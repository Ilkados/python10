from collections.abc import Callable

def mage_counter() -> Callable:
    """Create a counting closure starting from 1."""
    count = 0  # This variable lives in the 'enclosing' scope
    
    def counter() -> int:
        nonlocal count  # The bridge to the outer scope
        count += 1
        return count
    
    return counter

def spell_accumulator(initial_power: int) -> Callable:
    """Return a function that accumulates power over time."""
    current_power = initial_power
    
    def accumulator(power_to_add: int) -> int:
        nonlocal current_power
        current_power += power_to_add
        return current_power
    
    return accumulator

def enchantment_factory(enchantment_type: str) -> Callable:
    """Return a function that applies a specific enchantment to an item."""
    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"    

def memory_vault() -> dict[str, Callable]:
    """Create a memory management system with private storage."""
    vault = {}  
    
    def store(key: str, value: any) -> None:
        nonlocal vault
        vault[key] = value
        
    def recall(key: str) -> any:
        return vault.get(key, "Memory not found")
        
    return {"store": store, "recall": recall}
if __name__ == "__main__":
    
    print("Testing mage counter...")
    counter_a = mage_counter()
    print(f"counter_a call 1:{counter_a()}")
    print(f"counter_a call 2:{counter_a()}")
    counter_b = mage_counter()
    print(f"counter_b call 1:{counter_b()}")

    print("\nTesting spell accumulator...")
    accumulator1= spell_accumulator(100)
    print(f"Base 100, add 20: {accumulator1(20)}")
    accumulator2= spell_accumulator(100)
    print(f"Base 100, add 30: {accumulator2(30)}")

    print("\nTesting enchantment factory...")

    enchant = enchantment_factory("Flaming")
    print(enchant("Sword"))
    enchant1 = enchantment_factory("Frozen")
    print(enchant("Shield"))

    print("\nTesting memory vault...")
    valut = memory_vault()
    valut()