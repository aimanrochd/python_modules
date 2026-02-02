import sys


def ft_score_analytics():
    if len(sys.argv) > 1:
        scores = []
        try:
            for i in sys.argv:
                if i is sys.argv[0]:
                    continue
                scores += [int(i)]
        except ValueError:
            print("Error: You're Passing Non-Numeric Values")
        print(f"Scores processed: {scores}")
        total_players = len(scores)
        print(f"Total players: {total_players}")
        total_scores = sum(scores)
        print(f"Total score: {total_scores}")
        average = sum(scores) / total_players
        print(f"Average score: {average}")
        high_score = max(scores)
        print(f"High score: {high_score}")
        low_score = min(scores)
        print(f"Low score: {low_score}")
        range = high_score - low_score
        print(f"Score range: {range}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    ft_score_analytics()
