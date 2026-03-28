import functools
import operator
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    op_func = ops.get(operation, operator.add)
    return functools.reduce(op_func, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        'fire_enchant': functools.partial(base_enchantment, 50, 'Fire'),
        'ice_enchant': functools.partial(base_enchantment, 50, 'Ice'),
        'lightning_enchant': functools.partial(base_enchantment, 50,
                                               'Lightning')
    }


# The lru_cache decorator automatically caches the results of function calls
@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Without caching, this recursive call would be incredibly
    # slow for high numbers
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    # singledispatch creates a function that changes
    # behavior based on argument type
    @functools.singledispatch
    def cast_spell(arg: Any) -> str:
        return "Unknown spell type"

    @cast_spell.register(int)
    def _(arg: int) -> str:
        return f"Casts a damage spell with {arg} power"

    @cast_spell.register(str)
    def _(arg: str) -> str:
        return f"Casts enchantment: {arg}"

    @cast_spell.register(list)
    def _(arg: list) -> str:
        return f"Multi-casting {len(arg)} spells"

    return cast_spell


if __name__ == '__main__':

    print("Testing spell_reducer...")
    powers = [10, 20, 30, 40]
    print(f"add: {spell_reducer(powers, 'add')}")
    print(f"multiply: {spell_reducer(powers, 'multiply')}")
    print(f"Max: {spell_reducer(powers, 'max')}")
    print(f"Min: {spell_reducer(powers, 'min')}")

    print("\nTesting partial_enchanter...")

    def base_spell(power: int, element: str, target: str) -> str:
        return f"Casting {element} with {power} power at {target}"

    enchanters = partial_enchanter(base_spell)
    print(enchanters['fire_enchant']("Goblin"))
    print(enchanters['ice_enchant']("Dragon"))

    print("\nTesting memoized_fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell_dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(100))
    print(dispatcher("Invisibility"))
    print(dispatcher(["Fireball", "Heal", "Shield"]))
