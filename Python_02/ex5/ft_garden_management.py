class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 100

    def add_plant(
            self,
            plant_name: str,
            water_need: int = 5,
            sun_need: int = 8):
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        if plant_name in self.plants:
            raise PlantError(f"Plant '{plant_name}' already exists!")

        self.plants[plant_name] = {
            'water': water_need,
            'sun': sun_need
        }
        print(f"Added {plant_name} successfully")

    def water_plants(self):
        print("Opening watering system")

        try:
            for plant_name in self.plants:
                if self.water_tank < 10:
                    raise WaterError("Not enough water in tank")

                print(f"Watering {plant_name} - success")
                self.water_tank -= 10

        except WaterError as e:
            print(f"Error: {e}")
            raise

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, plant_name: str):
        if plant_name not in self.plants:
            raise PlantError(f"Plant '{plant_name}' not found in garden!")

        plant = self.plants[plant_name]
        water = plant['water']
        sun = plant['sun']

        if water < 1:
            raise PlantError(f"Water level {water} is too low (min 1)")
        if water > 10:
            raise PlantError(f"Water level {water} is too high (max 10)")
        if sun < 2:
            raise PlantError(f"Sunlight hours {sun} is too low (min 2)")
        if sun > 12:
            raise PlantError(f"Sunlight hours {sun} is too high (max 12)")

        print(f"{plant_name}: healthy (water: {water}, sun: {sun})")


def test_garden_management():
    print("=== Garden Management System ===\n")

    garden = GardenManager()

    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        garden.add_plant("lettuce", 15, 6)
    except PlantError as e:
        print(f"Error adding plant: {e}")

    try:
        garden.add_plant("", 5, 8)
    except PlantError as e:
        print(f"Error adding plant: {e}")
    print()

    print("Watering plants...")
    try:
        garden.water_plants()
    except WaterError as e:
        print(f"Watering failed: {e}")
    print()

    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato")
    except PlantError as e:
        print(f"Error checking tomato: {e}")

    try:
        garden.check_plant_health("lettuce")
    except PlantError as e:
        print(f"Error checking lettuce: {e}")
    print()

    print("Testing error recovery...")
    try:
        garden.water_tank = 5  # Set low water
        garden.water_plants()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    print()

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
