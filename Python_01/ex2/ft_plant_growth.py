class   Plant:
    """ A class to represent a plant in the garden """
    def __init__(self, name, height, age):
        """ Initialize a new Plant instance """
        self.name = name
        self.height = height
        self.age = age

    def grow(self, amount: int) -> None:
        """Increase the height of the plant by the specified amount."""
        self.height += amount
    def age_growth(self) -> None:
        """this method increase the age of a plant by 1 day"""
        self.age += 1
    def get_info(self) -> None:
        """this method give us information about the current plant status"""
        print(f"{self.name}: {self.height}cm, {self.age} days old")

def main():
    plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45)
    ]
    initial_heights = []
    total_plants = 0
    for p in plants:
        initial_heights = initial_heights + [p.height]
        total_plants += 1
    day = 1
    print(f"=== Day {day} ===")
    for plant in plants:
        plant.get_info()
    while day < 7:
        day += 1
        for plant in plants:
            plant.grow(1)
            plant.age_growth()
    print(f"=== Day {day} ===")
    for plant in plants:
        plant.get_info()
    print()
    total_plants = 0
    for i in plants:
        total_plants += 1
    i = 0
    while i < total_plants:
        current_plant = plants[i]
        growth = current_plant.height - initial_heights[i]
        print(f"Growth this week For {current_plant.name}: +{growth}cm")
        i += 1

if __name__ == "__main__":
    main()