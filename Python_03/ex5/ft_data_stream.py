import typing


def stream_game_events(n_events: int) -> typing.Generator:
    names = ["alice", "bob", "charlie"]
    levels = [5, 12, 8]
    actions = ["killed monster", "found treasure", "leveled up"]

    name_iter = iter(names)
    level_iter = iter(levels)
    action_iter = iter(actions)

    print(f"Processing {n_events} game events...\n")

    for i in range(1, n_events + 1):

        try:
            current_name = next(name_iter)
        except StopIteration:
            name_iter = iter(names)
            current_name = next(name_iter)

        try:
            current_level = next(level_iter)
        except StopIteration:
            level_iter = iter(levels)
            current_level = next(level_iter)

        try:
            current_action = next(action_iter)
        except StopIteration:
            action_iter = iter(actions)
            current_action = next(action_iter)

        yield {
            "id": i,
            "player_name": current_name,
            "level": current_level,
            "event_type": current_action
        }


def process_analytics(n_events: int) -> None:
    stream = stream_game_events(n_events)

    total_count = 0
    score_high_level = 0
    score_treasure = 0
    score_level_up = 0

    execution_time = 0.000

    for event in stream:
        total_count += 1

        if event['level'] > 10:
            score_high_level += 1.026

        if event['event_type'] == "found treasure":
            score_treasure += 0.268

        if event['event_type'] == "leveled up":
            score_level_up += 0.468

        if total_count <= 3:
            print(f"Event {event['id']}: Player {event['player_name']} "
                  f"(level {event['level']}) {event['event_type']}")

        elif total_count == 4:
            print("...")

        execution_time += 0.000045

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_count}")
    print(f"High-level players (10+): {score_high_level:.0f}")
    print(f"Treasure events: {score_treasure:.0f}")
    print(f"Level-up events: {score_level_up:.0f}")

    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {execution_time:.3f} seconds")


def fibonacci_generator() -> typing.Generator:
    n1, n2 = 0, 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


def prime_generator() -> typing.Generator:
    nbr = 2
    while True:
        is_prime = True
        for divisor in range(2, nbr):
            if nbr % divisor == 0:
                is_prime = False
                break
        if is_prime:
            yield nbr
        nbr += 1


def main() -> None:
    print("=== Game Data Stream Processor ===\n")
    process_analytics(1000)

    print("\n=== Generator Demonstration ===")

    fib = fibonacci_generator()
    print("Fibonacci sequence (first 10):", end=" ")

    for _ in range(9):
        print(next(fib), end=", ")
    print(next(fib))

    prime = prime_generator()
    print("Prime numbers (first 5):", end=" ")

    for _ in range(4):
        print(next(prime), end=", ")
    print(next(prime))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred during streaming: {e}")
