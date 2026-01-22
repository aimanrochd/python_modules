class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self._height = height
        self.plant_type = "Regular"

    def get_height(self) -> int:
        return self._height

    def set_height(self, value: int) -> None:
        if value < 0:
            print("Error: Height cannot be negative.")
        else:
            self._height = value

    def grow(self, amount: int) -> None:
        self.set_height(self._height + amount)
        print(f"{self.name} grew {amount}cm")

    def bloom(self) -> None:
        pass

    def get_info(self) -> str:
        return f"{self.name}: {self.get_height()}cm"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, flower_color: str) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = False
        self.plant_type = "Flowering"

    def bloom(self) -> None:
        self.is_blooming = True

    def get_info(self) -> str:
        status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.get_height()}cm, {self.flower_color} " \
               f"flowers ({status})"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, flower_color: str,
                 prize_points: int) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points
        self.plant_type = "Prize"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, Prize points: {self.prize_points}"


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []


class GardenManager:
    gardens = {}
    total_gardens = 0

    class GardenStats:
        def __init__(self) -> None:
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0

        def update_counts(self, plant: Plant) -> None:
            self.plants_added += 1
            if plant.plant_type == "Prize":
                self.prize_flowers += 1
            elif plant.plant_type == "Flowering":
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def get_report(self) -> str:
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_plants} regular, "
                    f"{self.flowering_plants} flowering, "
                    f"{self.prize_flowers} prize flowers")

    def __init__(self, owner_name: str) -> None:
        self.owner_name = owner_name
        self.garden = Garden(owner_name)
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens[owner_name] = self
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        self.garden.plants += [plant]
        self.stats.update_counts(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def collective_growth(self, amount: int) -> None:
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.garden.plants:
            plant.grow(amount)
            self.stats.total_growth += amount

    def calculate_score(self) -> int:
        score = 0
        for plant in self.garden.plants:
            score += 10
            score += plant.get_height()
            if plant.plant_type == "Prize":
                score += plant.prize_points
        return score

    def create_garden_network(cls, owners: list) -> None:
        for owner in owners:
            cls(owner)

    create_garden_network = classmethod(create_garden_network)

    def plant_height_validation(height: int) -> bool:
        return height >= 0

    plant_height_validation = staticmethod(plant_height_validation)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")

    GardenManager.create_garden_network(["Alice", "Bob"])
    alice = GardenManager.gardens["Alice"]
    bob = GardenManager.gardens["Bob"]

    bob.add_plant(Plant("Bob's Hidden Plant", 82))

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
