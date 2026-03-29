from typing import Callable, Any, Dict


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    if not isinstance(initial_power, int):
        raise TypeError("initial_power must be an integer")

    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        if not isinstance(power_to_add, int):
            raise TypeError("power_to_add must be an integer")
        total_power += power_to_add
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    if not isinstance(enchantment_type, str):
        raise TypeError("enchantment_type must be a string")

    def enchanter(item_name: str) -> str:
        if not isinstance(item_name, str):
            raise TypeError("item_name must be a string")
        return f"{enchantment_type} {item_name}"

    return enchanter


def memory_vault() -> Dict[str, Callable]:
    vault_storage: Dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        if not isinstance(key, str):
            raise TypeError("key must be a string")
        vault_storage[key] = value

    def recall(key: str) -> Any:
        if not isinstance(key, str):
            raise TypeError("key must be a string")
        return vault_storage.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    accum = spell_accumulator(10)
    print(f"Add 5 (Total): {accum(5)}")
    print(f"Add 20 (Total): {accum(20)}")

    print("\nTesting enchantment factory...")
    flame_enchant = enchantment_factory("Flaming")
    frost_enchant = enchantment_factory("Frozen")
    print(flame_enchant("Sword"))
    print(frost_enchant("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    vault['store']('spell_1', 'Fireball')
    print(vault['recall']('spell_1'))
    print(vault['recall']('unknown_spell'))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
