def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    # sorted() takes an iterable and a 'key' function.
    # The lambda extracts the 'power' value, and reverse=True sorts descending.
    return sorted(artifacts, key=lambda x: x.get('power', 0), reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    # filter() returns an iterator, so we wrap it in list() to match the
    # return type.
    # The lambda returns True if the mage's power is >= min_power.
    return list(filter(lambda x: x.get('power', 0) >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    # map() applies the lambda to every item in the list
    # Wrap in list() to return.
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    # max() and min() can take a 'key' argument powered by a lambda.
    max_power = max(mages, key=lambda x: x.get('power', 0)).get('power', 0)
    min_power = min(mages, key=lambda x: x.get('power', 0)).get('power', 0)

    # sum() doesn't take a 'key', so we use map()
    # with a lambda to extract powers first.
    total_power = sum(map(lambda x: x.get('power', 0), mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        'max_power': max_power,
        'min_power': min_power,
        'avg_power': avg_power
    }


if __name__ == '__main__':
    # Sample test data to prove it works during your defense
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
