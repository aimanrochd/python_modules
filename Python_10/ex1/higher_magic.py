from typing import Callable, Any, List, Tuple


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    if not callable(spell1) or not callable(spell2):
        raise TypeError("Both inputs must be callable functions")

    def combined(*args: Any, **kwargs: Any) -> Tuple[Any, Any]:
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    if not callable(base_spell):
        raise TypeError("base_spell must be a callable function")
    if not isinstance(multiplier, int):
        raise TypeError("multiplier must be an integer")

    def amplified(*args: Any, **kwargs: Any) -> Any:
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    if not callable(condition) or not callable(spell):
        raise TypeError("Both inputs must be callable functions")

    def conditional(*args: Any, **kwargs: Any) -> Any:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: List[Callable]) -> Callable:
    if not isinstance(spells, list):
        raise TypeError("spells must be a list of callables")
    if not all(callable(s) for s in spells):
        raise TypeError("All elements in spells must be callable")

    def sequence(*args: Any, **kwargs: Any) -> List[Any]:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


def main() -> None:
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


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
