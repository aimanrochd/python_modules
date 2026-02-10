def get_game_data() -> list[dict]:
    """
    Returns the hardcoded 'database' of players.
    Each player has: name, score, region, items, and achievements.
    """
    return [
        {
            "name": "alice",
            "score": 2300,
            "region": "north",
            "items": ["sword", "potion", "map"],
            "achievements": ["first_kill", "level_10", "treasure_hunter"]
        },
        {
            "name": "bob",
            "score": 1800,
            "region": "east",
            "items": ["shield", "potion"],
            "achievements": ["first_kill", "boss_slayer"]
        },
        {
            "name": "charlie",
            "score": 2150,
            "region": "north",
            "items": ["sword", "helmet", "armor"],
            "achievements": ["level_10", "boss_slayer", "speed_demon"]
        },
        {
            "name": "diana",
            "score": 4300,
            "region": "west",
            "items": ["staff", "potion", "robe"],
            "achievements": ["perfectionist", "level_10", "treasure_hunter"]
        },
        {
            "name": "eve",
            "score": 1200,
            "region": "east",
            "items": ["shield", "bread"],
            "achievements": ["first_kill"]
        }
    ]


def analyze_lists(players: list[dict]) -> None:

    high_scorers: list[str] = [player["name"] for player in players
                               if player["score"] > 2000]
    doubled_scores: list[int] = [player["score"] * 2 for player in players]
    active_players: list[str] = [player["name"] for player in players]

    print("=== List Comprehension Examples ===")
    print(f"High scorers (>2000): {high_scorers}")
    print(f"Scores doubled: {doubled_scores}")
    print(f"Active players: {active_players}\n")


def analyze_dicts(players: list[dict]) -> None:
    player_scores = {player["name"]: player["score"] for player in players}
    score_categories: list[str, int] = {
        "high": len([p for p in players if p["score"] > 2200]),
        "medium": len([p for p in players if 1500 <= p["score"] <= 2200]),
        "low": len([p for p in players if p["score"] < 1500])
    }
    achievement_counts: dict[str, int] = {
        p["name"]: len(p["items"])
        for p in players
    }
    print("=== Dict Comprehension Examples ===")
    print(f"Player scores: {player_scores}")
    print(f"Score categories: {score_categories}")
    print(f"Achievement counts: {achievement_counts}\n")


def analyze_sets(players: list[dict]) -> None:

    unique_players: set[str] = {player["name"] for player in players}
    unique_achievements: set[str] = {
        achievement
        for p in players
        for achievement in p["achievements"]
    }
    active_regions: set[str] = {player["region"] for player in players}
    print("=== Set Comprehension Examples ===")
    print(f"Unique players: {unique_players}")
    print(f"Unique achievements: {unique_achievements}")
    print(f"Active regions: {active_regions}\n")


def print_summary(players: list[dict]) -> None:
    all_players: list[str] = [player["name"] for player in players]
    total_players = len(all_players)
    scores: list[int] = [player["score"] for player in players]
    total_score = max(scores)
    average_score = total_score / total_players
    max_score: int = max([p["score"] for p in players])
    top_players_list: list[dict] = [p for p in players
                                    if p["score"] == max_score]
    best_player = top_players_list[0]
    unique_achievements: set[str] = {
        a for p in players
        for a in p["achievements"]
    }
    print("=== Combined Analysis ===")
    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {len(unique_achievements)}")
    print(f"Average score: {average_score}")
    print(
        f"Top performer: {best_player['name']} "
        f"({best_player['score']} points, "
        f"{len(best_player['achievements'])} achievements)"
    )


def main() -> None:
    data_base = get_game_data()
    analyze_lists(data_base)
    analyze_dicts(data_base)
    analyze_sets(data_base)
    print_summary(data_base)


if __name__ == "__main__":
    main()
