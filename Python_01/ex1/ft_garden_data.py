class Plant:
    """ A class to represent a plant in the garden """
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with a name, height and age"""
        self.name = name
        self.height = height
        self.age = age


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]
    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
