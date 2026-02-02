def ft_achievement_tracker():
    """"""
    alice = {
            'name': 'alice',
            'achievements': {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    }
    bob = {
        'name': 'bob',
        'achievements': {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    }
    charlie = {
        'name': 'charlie',
        'achievements': {'level_10', 'treasure_hunter', 'boss_slayer', 'speed_demon', 'perfectionist'}
    }

    players = alice, bob, charlie
    for player in players:
        print(f"Player {player['name']} achievements: {player['achievements']}")
    
    return players


def ft_achievements_analytics(players):
    """"""
    unique_achievements = set().union(players[0]['achievements'],
                                       players[1]['achievements'],
                                       players[2]['achievements'])
    print(f"All unique achievements: {unique_achievements}")
    print(f"Total unique achievements: {len(unique_achievements)}\n")

    common_achievements = players[0]['achievements'].intersection(players[1]['achievements'],
                                              players[2]['achievements'])
    print(f"Common to all players: {common_achievements}")

    rare_alice = players[0]['achievements'].difference(players[1]['achievements'].union(players[2]['achievements']))
    rare_bob = players[1]['achievements'].difference(players[0]['achievements'].union(players[2]['achievements']))
    rare_charlie = players[2]['achievements'].difference(players[0]['achievements'].union(players[1]['achievements']))
    rare_achievements = rare_alice.union(rare_bob, rare_charlie)
    print(f"Rare achievements (1 player): {rare_achievements}\n")

    alice_vs_bob = players[0]['achievements'].intersection(players[1]['achievements'])
    print(f"Alice vs Bob common: {alice_vs_bob}")
    alice_unique = players[0]['achievements'].difference(players[1]['achievements'])
    print(f"Alice unique: {alice_unique}")
    bob_unique = players[1]['achievements'].difference(players[0]['achievements'])
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    players = ft_achievement_tracker()
    print()
    print("=== Achievement Analytics ===")
    ft_achievements_analytics(players)