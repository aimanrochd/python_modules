class Plant:
    """The Base Class representing a generic plant."""
    def __init__(self, name: str, height: int) -> None:
        """Initializes the plant with a name and height."""
        self.name = name
        self._height = 0
        self.plant_type = "Regular"
        self.set_height(height)

    def get_height(self) -> int:
        """Returns the current height of the plant."""
        return self._height

    def set_height(self, value: int) -> None:
        """Sets the plant's height after validation."""
        if value < 0:
            print("Error: Height cannot be negative.")
        else:
            self._height = value

    def grow(self, amount: int) -> None:
        """Increases the plant's height by the given amount."""
        self.set_height(self._height + amount)
        print(f"{self.name} grew {amount}cm")

    def bloom(self) -> None:
        """Placeholder method for blooming behavior."""
        pass

    def get_info(self) -> str:
        """Returns a string summary of the plant's basic info."""
        return f"{self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    """Represents a plant that can bloom, inheriting from Plant."""
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        """Initializes the flowering plant with color attributes."""
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = False
        self.plant_type = "Flowering"

    def bloom(self) -> None:
        """Sets the blooming status to True."""
        self.is_blooming = True

    def get_info(self) -> str:
        """Returns info including flower color and blooming status."""
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.get_height()}cm, {self.flower_color} " \
               f"flowers ({status})"


class PrizeFlower(FloweringPlant):
    """Represents a special flower that has prize points."""
    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int) -> None:
        """Initializes the prize flower with specific points."""
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points
        self.plant_type = "Prize"

    def get_info(self) -> str:
        """Returns info including the prize points."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class Garden:
    """Represents the physical garden holding a list of plants."""
    def __init__(self, owner: str) -> None:
        """Initializes the garden with an owner and an empty plant list."""
        self.owner = owner
        self.plants = []


class GardenManager:
    """Manages garden operations, stats, and the garden network."""
    gardens = {}
    total_gardens = 0

    class GardenStats:
        """Helper class for tracking garden statistics internally."""
        def __init__(self) -> None:
            """Initializes the statistical counters."""
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0

        def update_counts(self, plant: Plant) -> None:
            """Updates counters based on the type of plant added."""
            self.plants_added += 1
            if plant.plant_type == "Prize":
                self.prize_flowers += 1
            elif plant.plant_type == "Flowering":
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def get_report(self) -> str:
            """Returns a formatted string of the current statistics."""
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_plants} regular, "
                    f"{self.flowering_plants} flowering, "
                    f"{self.prize_flowers} prize flowers")

    def __init__(self, owner_name: str) -> None:
        """Initializes the manager, creates a garden, and registers it."""
        self.owner_name = owner_name
        self.garden = Garden(owner_name)
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens[owner_name] = self
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant, details: bool = True) -> None:
        """Adds a plant to the garden and updates statistics."""
        self.garden.plants += [plant]
        self.stats.update_counts(plant)
        if details:
            print(f"Added {plant.name} to {self.owner_name}'s garden")

    def collective_growth(self, amount: int) -> None:
        """Triggers the grow method for every plant in the garden."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.garden.plants:
            plant.grow(amount)
            self.stats.total_growth += amount

    def calculate_score(self) -> int:
        """Calculates the total score based on height and prize points."""
        score = 0
        for plant in self.garden.plants:
            score += 10
            score += plant.get_height()
            if plant.plant_type == "Prize":
                score += plant.prize_points
        return score

    def create_garden_network(cls, owners: list) -> None:
        """Class method factory to create multiple garden managers at once."""
        for owner in owners:
            cls(owner)

    create_garden_network = classmethod(create_garden_network)

    def plant_height_validation(height: int) -> bool:
        """Static utility method to validate if height is non-negative."""
        return height >= 0

    plant_height_validation = staticmethod(plant_height_validation)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    GardenManager.create_garden_network(["Alice", "Bob"])
    alice = GardenManager.gardens["Alice"]
    bob = GardenManager.gardens["Bob"]

    bob.add_plant(Plant("Bob's Hidden Plant", 82), False)

    alice_plants = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]

    for plant in alice_plants:
        alice.add_plant(plant)
    print()

    alice.collective_growth(1)
    print()

    for plant in alice.garden.plants:
        plant.bloom()

    print(f"=== {alice.owner_name}'s Garden Report ===")
    print("Plants in garden:")
    for plant in alice.garden.plants:
        print(f"- {plant.get_info()}")
    print()

    print(alice.stats.get_report())
    print()

    print(f"Height validation test: "
          f"{GardenManager.plant_height_validation(10)}")

    print(f"Garden scores - {alice.owner_name}: {alice.calculate_score()}, "
          f"{bob.owner_name}: {bob.calculate_score()}")

    print(f"Total gardens managed: {GardenManager.total_gardens}")
