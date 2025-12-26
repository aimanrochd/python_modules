class Plant:
    """Blueprint for a garden plant."""
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def grow(self) -> None:
        "Increases the plant's height by 1cm"
        self.height += 1

    def age_one_day(self) -> None:
        "Increases the plant's age by 1 day"
        self.age += 1

    def get_info(self) -> str:
        "prints a formatted string of the plant's current status"
        return (f"{self.name}: {self.height}cm, {self.age} days old")
            
if __name__ == "__main__":
    plant = Plant("Rose", 25, 30)

    initial_height = plant.height

    print("=== Day 1 ===")
    print(plant.get_info())
    i = 1
    while i < 7:
        plant.age_one_day()
        plant.grow()
        i += 1
    print("=== Day 7 ===")
    print(plant.get_info())
    
    growth = plant.height - initial_height
    print(f"Growth this week: +{growth}cm")
    