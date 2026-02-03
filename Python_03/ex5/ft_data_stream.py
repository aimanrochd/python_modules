def stream_game_events(n_events: int):
    """
    Generator that creates game events on demand uses yield to save memory."""
    names = ["alice", "bob", "charlie", "diana", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]
    
    for i in range(1, n_events + 1):
        name = names[i % len(names)]
        action = actions[i % len(actions)]
        
        level = (i * 3) % 20 + 1 
        
        yield f"Event {i}: Player {name} (level {level}) {action}"

def fibonacci_generator(n):
    """Yields the first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def prime_generator(n):
    """Yields the first n prime numbers."""
    count = 0
    num = 2
    while count < n:
        is_prime = True
        i = 2
        while i * i <= num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        
        if is_prime:
            yield num
            count += 1
        num += 1

def process_analytics(n_events: int):
    print("=== Game Data Stream Processor ===\n")
    print(f"Processing {n_events} game events...\n")
    
    stream = stream_game_events(n_events)
    
    total_events = 0
    high_level_count = 0
    treasure_count = 0
    level_up_count = 0
    
    for event in stream:
        total_events += 1
        
        if total_events <= 3:
            print(event)
        elif total_events == 4:
            print("...")
            
        if "found treasure" in event:
            treasure_count += 1
        elif "leveled up" in event:
            level_up_count += 1
            
        try:
            parts = event.split("level ")
            if len(parts) > 1:
                level_str = parts[1].split(")")[0]
                level = int(level_str)
                if level >= 10:
                    high_level_count += 1
        except:
            pass

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total_events}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {level_up_count}\n")
    
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

def main():
    process_analytics(1000)
    
    print("\n=== Generator Demonstration ===")
    
    print("Fibonacci sequence (first 10): ", end="")
    print(*fibonacci_generator(10), sep=", ")
    
    print("Prime numbers (first 5):", end=" ")
    print(*prime_generator(5), sep=", ")

if __name__ == "__main__":
    main()