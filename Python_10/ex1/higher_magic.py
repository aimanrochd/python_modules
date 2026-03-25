from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    # We define an inner function that accepts any arguments (*args, **kwargs)
    def combined(*args: Any, **kwargs: Any) -> tuple:
        # It calls both spells with those exact same arguments
        # and returns a tuple
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    # We return the NEW function itself, not the result of the function
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args: Any, **kwargs: Any) -> Any:
        # We call the original spell, then multiply its result
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(*args: Any, **kwargs: Any) -> Any:
        # We pass the arguments to the condition first
        if condition(*args, **kwargs):
            # If True, we cast the spell with those arguments
            return spell(*args, **kwargs)
        # If False, it fizzles
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args: Any, **kwargs: Any) -> list:
        # We use a list comprehension to cast every spell in the list in order
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == '__main__':
    # --- Sample functions to test your code during the defense ---
    def fireball(target: str = "Dragon") -> str:
        return f"Fireball hits {target}"

    def heal(target: str = "Dragon") -> str:
        return f"Heals {target}"

    def damage_spell(power: int = 10) -> int:
        return power

    def is_powerful(power: int = 10) -> bool:
        return power > 50

    # 1. Testing spell_combiner
    print("Testing spell_combiner...")
    combined_spell = spell_combiner(fireball, heal)
    res1, res2 = combined_spell("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    # 2. Testing power_amplifier
    print("\nTesting power_amplifier...")
    mega_fireball = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell(10)}, Amplified: {mega_fireball(10)}")

    # 3. Testing conditional_caster
    print("\nTesting conditional_caster...")
    safe_cast = conditional_caster(is_powerful, damage_spell)
    print(f"Cast with 100 power: {safe_cast(100)}")
    print(f"Cast with 20 power: {safe_cast(20)}")

    # 4. Testing spell_sequence
    print("\nTesting spell_sequence...")
    def zap() -> str: return "Zap!"
    def boom() -> str: return "Boom!"
    seq = spell_sequence([zap, boom])
    print(f"Sequence result: {seq()}")
