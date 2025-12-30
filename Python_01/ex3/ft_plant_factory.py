class Plant:
    """Blueprint for a garden plant."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age


def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    total = 0
    for p in plants:
        print(f"Created: {p.name} ({p.height}cm, {p.age} days)")
        total += 1
    print()
    print(f"Total plants created: {total}")


if __name__ == "__main__":
    main()
