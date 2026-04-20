def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda artifact: artifact["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "* " + spell + " *", spells))


def mage_stats(mages: list[dict]) -> dict:
    max_power = max(mages, key=lambda mage: mage["power"])["power"]
    min_power = min(mages, key=lambda mage: mage["power"])["power"]
    avg_power = round(sum(map(lambda mage: mage["power"], mages)) / len(mages), 2)

    return {
        "max_power": max_power,
        "min_power": min_power,
        "avg_power": avg_power,
    }


if __name__ == "__main__":
    artifact_list = [
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
            f"comes before {second_artifact['name']} ({second_artifact['power']} power)"
        )

    mage_list = [
        {"name": "Ikdos", "power": 90, "element": "arcane"},
        {"name": "Miarmi", "power": 23, "element": "fire"},
        {"name": "Dagger", "power": 45, "element": "earth"},
    ]

    filtered_mage_list = power_filter(mage_list, 24)

    print("\nTesting power filter...")
    for mage in filtered_mage_list:
        print(f"{mage['name']} ({mage['power']} power)")

    spell_list = ["fireball", "heal", "shield"]
    transformed_spell_list = spell_transformer(spell_list)

    print("\nTesting spell transformer...")
    print(" ".join(transformed_spell_list))

    mage_statistics = mage_stats(mage_list)

    print("\nTesting mage stats...")
    print(
        f"max_power: {mage_statistics['max_power']}, "
        f"min_power: {mage_statistics['min_power']}, "
        f"avg_power: {mage_statistics['avg_power']}"
    )