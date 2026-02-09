def ft_achievement_tracker() -> tuple:
    alice = {
            'name': 'alice',
            'achievements': {'first_kill', 'level_10',
                             'treasure_hunter', 'speed_demon'}
    }
    bob = {
        'name': 'bob',
        'achievements': {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    }
    charlie = {
        'name': 'charlie',
        'achievements': {'level_10', 'treasure_hunter', 'boss_slayer',
                         'speed_demon', 'perfectionist'}
    }

    players = alice, bob, charlie
    for player in players:
        print(f"Player {player['name']} achievements: "
              f"{player['achievements']}")

    return players


def ft_achievements_analytics(players) -> None:
    # UNION: Combines all sets into one, automatically removing duplicates to find every unique achievement available.
    unique_achievements = set().union(
        players[0]['achievements'],
        players[1]['achievements'],
        players[2]['achievements']
    )
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    # INTERSECTION: Finds only the elements that exist in ALL three sets simultaneously (shared by everyone).
    common_achievements = players[0]['achievements'].intersection(
        players[1]['achievements'],
        players[2]['achievements']
    )
    print(f"Common to all players: {common_achievements}")

    # DIFFERENCE & UNION: Subtracts the combined achievements of Bob and Charlie from Alice to find what ONLY Alice has.
    rare_alice = players[0]['achievements'].difference(
        players[1]['achievements'].union(players[2]['achievements'])
    )
    # DIFFERENCE & UNION: Subtracts Alice and Charlie from Bob to find what ONLY Bob has.
    rare_bob = players[1]['achievements'].difference(
        players[0]['achievements'].union(players[2]['achievements'])
    )
    # DIFFERENCE & UNION: Subtracts Alice and Bob from Charlie to find what ONLY Charlie has.
    rare_charlie = players[2]['achievements'].difference(
        players[0]['achievements'].union(players[1]['achievements'])
    )
    
    # UNION: Combines the isolated unique achievements from each player into one "Rare" list.
    rare_achievements = rare_alice.union(rare_bob, rare_charlie)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    # INTERSECTION: Finds achievements shared specifically between Alice and Bob.
    alice_vs_bob = players[0]['achievements'].intersection(
        players[1]['achievements']
    )
    print(f"Alice vs Bob common: {alice_vs_bob}")

    # DIFFERENCE: Finds achievements Alice owns that Bob does NOT have (Alice minus Bob).
    alice_unique = players[0]['achievements'].difference(
        players[1]['achievements']
    )
    print(f"Alice unique: {alice_unique}")

    # DIFFERENCE: Finds achievements Bob owns that Alice does NOT have (Bob minus Alice).
    bob_unique = players[1]['achievements'].difference(
        players[0]['achievements']
    )
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    players = ft_achievement_tracker()
    print()
    print("=== Achievement Analytics ===")
    ft_achievements_analytics(players)
