from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    current_power = initial_power

    def accumulator(power_to_add: int) -> int:
        nonlocal current_power
        current_power += power_to_add
        return current_power

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"

    return enchant


def memory_vault() -> dict[str, Callable]:
    vault = {}

    def store(key: str, value: Any) -> None:
        vault[key] = value

    def recall(key: str) -> Any:
        return vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator(20)}")
    print(f"Base 100, add 30: {accumulator(30)}")

    print("\nTesting enchantment factory...")
    enchant = enchantment_factory("Flaming")
    print(enchant("Sword"))
    enchant1 = enchantment_factory("Frozen")
    print(enchant1("Shield"))

    print("\nTesting memory vault...")
    result = memory_vault()
    result["store"]("secret", 42)
    print("Store 'secret' = 42")
    print(f"Recall 'secret': {result['recall']('secret')}")
    print(f"Recall 'unknown': {result['recall']('unknown')}")