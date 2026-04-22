from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Return a function that calls both spells and returns both results."""

    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))

    return combined_spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    """Return a spell with multiplied power before casting."""

    def amplified_spell(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    """Return a spell that only casts if a condition is true."""

    def gatekeeper(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"

    return gatekeeper


def spell_sequence(spells: list[Callable]) -> Callable:
    """Return a function that casts all spells in order."""

    def sequence_runner(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]

    return sequence_runner


def high_power_only(target: str, power: int) -> bool:
    del target
    return power > 100


if __name__ == "__main__":
    print("Test spell combiner")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))

    print("\nTest power amplifier")
    mega_fire = power_amplifier(fireball, 3)
    print(f"Amplified: {mega_fire('Dragon', 10)}")

    print("\nTest conditional caster")
    gated_heal = conditional_caster(high_power_only, heal)
    print(f"Low power check: {gated_heal('Mage', 50)}")
    print(f"High power check: {gated_heal('Mage', 150)}")

    print("\nTest spell sequence")
    combo = spell_sequence([fireball, heal])
    print(f"Sequence results: {combo('Orc', 20)}")
