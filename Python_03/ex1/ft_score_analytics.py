import sys


def ft_score_analytics() -> None:
    if len(sys.argv) > 1:
        scores = []
        try:
            for arg in sys.argv[1:]:
                scores += [int(arg)]
        except ValueError:
            print("Error: Non valid value found. "
                  "Please provide integers only.")
            return
        print(f"Scores processed: {scores}")

        total_players = len(scores)
        total_scores = sum(scores)

        print(f"Total players: {total_players}")
        print(f"Total score: {total_scores}")

        average = total_scores / total_players
        high_score = max(scores)
        low_score = min(scores)
        score_range = high_score - low_score

        print(f"Average score: {average:.1f}")
        print(f"High score: {high_score}")
        print(f"Low score: {low_score}")
        print(f"Score range: {score_range}")
    else:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")


if __name__ == "__main__":
    try:
        print("=== Player Score Analytics ===")
        ft_score_analytics()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
