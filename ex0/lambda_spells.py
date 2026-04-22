from typing import TypedDict


class Artifact(TypedDict):
    name: str
    power: int
    type: str


class Mage(TypedDict):
    name: str
    power: int
    element: str


def artifact_sorter(artifacts: list[Artifact]) -> list[Artifact]:
    return sorted(
        artifacts,
        key=lambda artifact: artifact["power"],
        reverse=True,
    )


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    return [mage for mage in mages if mage["power"] >= min_power]


def spell_transformer(spells: list[str]) -> list[str]:
    return [f"* {spell} *" for spell in spells]


def mage_stats(mages: list[Mage]) -> dict[str, float]:
    max_power = max(mage["power"] for mage in mages)
    min_power = min(mage["power"] for mage in mages)
    avg_power = round(sum(mage["power"] for mage in mages) / len(mages), 2)

    return {
        "max_power": float(max_power),
        "min_power": float(min_power),
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    artifact_list: list[Artifact] = [
        {"name": "Crystal Orb", "power": 85, "type": "focus"},
        {"name": "Fire Staff", "power": 92, "type": "weapon"},
        {"name": "Moon Dagger", "power": 78, "type": "blade"},
    ]

    sorted_artifact_list = artifact_sorter(artifact_list)

    print("Testing artifact sorter...")
    if len(sorted_artifact_list) >= 2:
        first_artifact = sorted_artifact_list[0]
        second_artifact = sorted_artifact_list[1]
        print(
            f"{first_artifact['name']} ({first_artifact['power']} power) "
            f"comes before {second_artifact['name']} "
            f"({second_artifact['power']} power)"
        )
    mages = [
        {"name": "Morgan", "power": 93, "element": "shadow"},
        {"name": "Sage", "power": 75, "element": "fire"},
        {"name": "Casey", "power": 77, "element": "ice"},
        {"name": "Luna", "power": 95, "element": "lightning"},
        {"name": "Zara", "power": 65, "element": "ice"},
    ]

    filtered_mage_list = power_filter(mages, 24)

    print("\nTesting power filter...")
    for mage in filtered_mage_list:
        print(f"{mage['name']} ({mage['power']} power)")

    spell_list = ["fireball", "heal", "shield"]
    transformed_spell_list = spell_transformer(spell_list)

    print("\nTesting spell transformer...")
    print(" ".join(transformed_spell_list))

    mage_statistics = mage_stats(filtered_mage_list)

    print("\nTesting mage stats...")
    print(
        f"max_power: {mage_statistics['max_power']}, "
        f"min_power: {mage_statistics['min_power']}, "
        f"avg_power: {mage_statistics['avg_power']}"
    )
