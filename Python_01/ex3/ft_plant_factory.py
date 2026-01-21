class Plant:
    """Blueprint for a garden plant."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with a name, height and age"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    total = 0
    for plant in plants:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        total += 1
    print()
    print(f"Total plants created: {total}")
