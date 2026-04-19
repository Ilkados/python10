from collections.abc import Callable

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell

combined = spell_combiner(fireball, heal)
print(combined("Dragon", 10))