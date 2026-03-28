import time
import functools
from typing import Any


def spell_timer(func: callable) -> callable:
    # @functools.wraps preserves the original function's name and metadata
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    # Because this decorator takes an argument (min_power), we need three
    # levels of functions
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = None

            # Extract 'power' whether it was passed as a keyword or positional
            # argument
            if 'power' in kwargs:
                power = kwargs['power']
            else:
                # Find the first integer in the arguments to handle both
                # standard functions
                # and class methods (where args[0] is 'self')
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break

            # Validate the extracted power against the minimum required
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable) -> callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}"
                          f"/{max_attempts})")

            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    # Apply our custom decorator to require power >= 10
    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == '__main__':

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()

    # Testing static method
    print(MageGuild.validate_mage_name("Gandalf the White"))
    print(MageGuild.validate_mage_name("A1"))

    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    print("\nTesting retry_spell...")
    fail_count = 0

    @retry_spell(max_attempts=3)
    def unstable_spell() -> str:
        global fail_count
        fail_count += 1
        if fail_count < 3:
            raise ValueError("Fizzle!")
        return "Stable cast!"

    print(unstable_spell())
