def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x.get('power', 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x.get('power', 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    max_power = max(map(lambda x: x.get('power', 0), mages))
    min_power = min(map(lambda x: x.get('power', 0), mages))
    avg_power = round(
        sum(map(lambda x: x.get('power', 0), mages)) / len(mages), 2
    )

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == '__main__':
    sample_artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'Orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'Staff'}
    ]

    sample_mages = [
        {'name': 'Alex', 'power': 100, 'element': 'Fire'},
        {'name': 'Jordan', 'power': 50, 'element': 'Water'},
        {'name': 'Riley', 'power': 150, 'element': 'Earth'}
    ]

    sample_spells = ["fireball", "heal", "shield"]

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(sample_artifacts)
    for art in sorted_artifacts:
        print(f"{art['name']} ({art['power']} power)")

    print("\nTesting spell transformer...")
    transformed = spell_transformer(sample_spells)
    for spell in transformed:
        print(spell)

    print("\nTesting power filter (min 100)...")
    filtered_mages = power_filter(sample_mages, 100)
    print([m['name'] for m in filtered_mages])

    print("\nTesting mage stats...")
    print(mage_stats(sample_mages))
