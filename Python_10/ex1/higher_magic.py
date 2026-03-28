from typing import Any


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args: Any, **kwargs: Any) -> tuple:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditional(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args: Any, **kwargs: Any) -> list:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == '__main__':
    def fireball(target: str = "Dragon") -> str:
        return f"Fireball hits {target}"

    def heal(target: str = "Dragon") -> str:
        return f"Heals {target}"

    def damage_spell(power: int = 10) -> int:
        return power

    def is_powerful(power: int = 10) -> bool:
        return power > 50

    print("Testing spell_combiner...")
    combined_spell = spell_combiner(fireball, heal)
    res1, res2 = combined_spell("Dragon")
    print(f"Combined spell result: {res1}, {res2}")

    print("\nTesting power_amplifier...")
    mega_fireball = power_amplifier(damage_spell, 3)
    print(f"Original: {damage_spell(10)}, Amplified: {mega_fireball(10)}")

    print("\nTesting conditional_caster...")
    safe_cast = conditional_caster(is_powerful, damage_spell)
    print(f"Cast with 100 power: {safe_cast(100)}")
    print(f"Cast with 20 power: {safe_cast(20)}")

    print("\nTesting spell_sequence...")
    def zap() -> str: return "Zap!"
    def boom() -> str: return "Boom!"
    seq = spell_sequence([zap, boom])
    print(f"Sequence result: {seq()}")
