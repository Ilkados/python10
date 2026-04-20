from collections.abc import Callable

def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"

def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"

def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Returns a function that calls both spells and returns a tuple of results[cite: 222, 224]."""
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell

def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Returns a spell where the power is multiplied before casting[cite: 227, 228]."""
    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified_spell

def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Returns a spell that only casts if a condition is True[cite: 230, 231]."""
    def gatekeeper(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return 'Spell fizzled'
    return gatekeeper

def spell_sequence(spells: list[Callable]) -> Callable:
    """Returns a function that casts all spells in the list in order[cite: 234, 235]."""
    def sequence_runner(target: str, power: int) -> list[str]:
        return [s(target, power) for s in spells]
    return sequence_runner

if __name__ == "__main__":

    print("Test spell combiner")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))
    
    print("\nTest Power Amplifier")
    mega_fire = power_amplifier(fireball, 3)
    print(f"Amplified: {mega_fire('Dragon', 10)}") 

    print("\nTest Conditional Caster")
    def high_power_only(target: str, power: int) -> bool:
        return power > 100
    gated_heal = conditional_caster(high_power_only, heal)
    print(f"Low power check: {gated_heal('Mage', 50)}")
    print(f"High power check: {gated_heal('Mage', 150)}")

    print("\nTest Spell Sequence")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence results: {combo('Orc', 20)}")