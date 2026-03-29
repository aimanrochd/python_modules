import time
import functools
from typing import Callable, Any


def spell_timer(func: Callable) -> Callable:
    if not callable(func):
        raise TypeError("func must be a callable function")

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    if not isinstance(min_power, int):
        raise TypeError("min_power must be an integer")

    def decorator(func: Callable) -> Callable:
        if not callable(func):
            raise TypeError("func must be a callable function")

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            power = None
            if 'power' in kwargs:
                power = kwargs['power']
            else:
                for arg in args:
                    if isinstance(arg, int):
                        power = arg
                        break
            if power is not None and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    if not isinstance(max_attempts, int) or max_attempts < 1:
        raise ValueError("max_attempts must be a positive integer")

    def decorator(func: Callable) -> Callable:
        if not callable(func):
            raise TypeError("func must be a callable function")

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
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if len(name) < 3:
            return False
        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


fail_count = 0


@retry_spell(max_attempts=3)
def unstable_spell() -> str:
    global fail_count
    fail_count += 1
    if fail_count < 3:
        raise ValueError("Fizzle!")
    return "Stable cast!"


def main() -> None:
    print("Testing spell timer...")

    @spell_timer
    def fireball() -> str:
        time.sleep(0.101)
        return "Fireball cast!"

    print(f"Result: {fireball()}")

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Gandalf the White"))
    print(MageGuild.validate_mage_name("A1"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))

    print("\nTesting retry_spell...")
    print(unstable_spell())


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
