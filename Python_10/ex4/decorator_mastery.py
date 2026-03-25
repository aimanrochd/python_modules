import time
import functools
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    # @functools.wraps preserves the original function's name and metadata
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()

        # Execute the actual function
        result = func(*args, **kwargs)

        end_time = time.time()
        # Calculate time and format to 3 decimal places
        elapsed = end_time - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    # Because this decorator takes an argument (min_power), we need three
    # levels of functions
    def decorator(func: Callable) -> Callable:
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


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    # If it succeeds, return the result immediately
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {attempt}"
                          f"/{max_attempts})")

            # If the loop finishes and all attempts failed
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        # Check if the name is at least 3 characters and only contains
        # letters/spaces
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    # Apply our custom decorator to require power >= 10
    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == '__main__':
    # --- Sample outputs matching the subject's expected output ---

    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)  # Simulate the spell taking some time to cast
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()

    # Testing static method
    print(MageGuild.validate_mage_name("Gandalf the White"))  # Expected: True
    print(MageGuild.validate_mage_name("A1"))                 # Expected: False

    # Testing instance method with power validator decorator
    print(guild.cast_spell("Lightning", 15))  # Expected: Success
    print(guild.cast_spell("Spark", 5))       # Expected: Insufficient power

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
