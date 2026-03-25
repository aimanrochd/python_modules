from typing import Callable, Any


def mage_counter() -> Callable:
    # This variable is trapped inside the outer function's scope
    count = 0

    def counter() -> int:
        # nonlocal tells Python to use and modify the 'count' from mage_counter
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal total_power
        total_power += power_to_add
        return total_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchanter(item_name: str) -> str:
        # It remembers 'enchantment_type' from the outer scope
        return f"{enchantment_type} {item_name}"

    # Make sure this return is OUTSIDE the enchanter function,
    # aligned with the 'def enchanter' line!
    return enchanter


def memory_vault() -> dict[str, Callable]:
    # This dictionary acts as our private, hidden memory storage
    vault_storage: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        vault_storage[key] = value

    def recall(key: str) -> Any:
        return vault_storage.get(key, "Memory not found")

    return {
        'store': store,
        'recall': recall
    }


if __name__ == '__main__':
    # --- Sample outputs matching the subject requirements ---

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
