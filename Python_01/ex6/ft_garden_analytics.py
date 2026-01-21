class Plant:
    """Base class for all plants."""
    def __init__(self, name: str, height: int) -> None:
        """Initializes the plant with a name and height"""
        self.name = name
        self._height = height
        self.plant_type = "Regular"

    def grow(self, amount: int) -> None:
        """Increases plant height by amount."""
        self._height += amount
        print(f"{self.name} grew {amount}cm")

    def get_info(self) -> str:
        """Returns basic plant info."""
        return f"{self.name}: {self._height}cm"


class FloweringPlant(Plant):
    """Represents a plant that can bloom."""
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        """Initializes the plant with a name, height and flower_color"""
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = False
        self.plant_type = "Flowering"

    def bloom(self) -> None:
        """Sets the plant to blooming state."""
        self.is_blooming = True

    def get_info(self) -> str:
        """Returns info including flower color and status."""
        if self.is_blooming:
            status = "blooming"
        else:
            status = "not blooming"
        return f"{self.name}: {self._height}cm, {self.flower_color} " \
               f"flowers ({status})"


class PrizeFlower(FloweringPlant):
    """Represents a flower with prize points."""
    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int) -> None:
        """Initializes the plant with a name, height, flower_color
        and prize_points"""
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points
        self.plant_type = "Prize"

    def get_info(self) -> str:
        """Adds prize points to the info string."""
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class Garden:
    """Represents the physical garden holding the plants."""
    def __init__(self, owner: str) -> None:
        """Initializes the garden with an owner and empty plant list"""
        self.owner = owner
        self.plants: list[Plant] = []


class GardenManager:
    """Manages garden operations and statistics."""
    gardens: dict = {}
    total_gardens: int = 0

    class GardenStats:
        """Helper class for tracking garden statistics."""
        def __init__(self) -> None:
            """initialize the instance with some starting values"""
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0

        def update_counts(self, plant: Plant) -> None:
            """Updates counters based on plant type."""
            self.plants_added += 1
            if plant.plant_type == "Prize":
                self.prize_flowers += 1
            elif plant.plant_type == "Flowering":
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def get_report(self) -> str:
            """Returns a formatted statistics string."""
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_plants} regular, "
                    f"{self.flowering_plants} flowering, "
                    f"{self.prize_flowers} prize flowers")

    def __init__(self, owner_name: str) -> None:
        """Initializes the garden manager with the owner name"""
        self.owner_name = owner_name
        self.garden = Garden(owner_name)
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens[owner_name] = self
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant and updates stats."""
        self.garden.plants.append(plant)
        self.stats.update_counts(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def collective_growth(self, amount: int) -> None:
        """Grows all plants in the garden."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.garden.plants:
            plant.grow(amount)
            self.stats.total_growth += amount

    def calculate_score(self) -> int:
        """Calculates total garden score."""
        score = 0
        for plant in self.garden.plants:
            score += 10
            score += plant._height
            if plant.plant_type == "Prize":
                score += plant.prize_points
        return score

    def create_garden_network(cls, owners: list[str]) -> None:
        """Factory method to create multiple gardens."""
        for owner in owners:
            cls(owner)

    create_garden_network = classmethod(create_garden_network)

    def plant_height_validation(height: int) -> bool:
        """Checks if height is valid (positive)."""
        return height >= 0

    plant_height_validation = staticmethod(plant_height_validation)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    GardenManager.create_garden_network(["Alice", "Bob"])

    alice = GardenManager.gardens["Alice"]
    bob = GardenManager.gardens["Bob"]

    bob_plant = Plant("Bob's Hidden Plant", 82)
    bob.add_plant(bob_plant)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    print()
    alice.collective_growth(1)

    rose.bloom()
    sunflower.bloom()

    print()
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