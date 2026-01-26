class GardenError(Exception):
    """Base exception for garden-related problems"""
    pass


class PlantError(GardenError):
    """Exception for plant-specific problems"""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems"""
    pass


class GardenManager:
    """Manages garden operations with error handling"""
    
    def __init__(self):
        """Initialize garden manager"""
        self.plants = []
    
    def add_plant(self, plant_name: str) -> None:
        """Add a plant to the garden"""
        try:
            if plant_name == "":
                raise PlantError("Plant name cannot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as e:
            print(f"Error adding plant: {e}")
    
    def water_plants(self) -> None:
        """Water all plants in the garden"""
        try:
            print("Opening watering system")
            for plant in self.plants:
                if plant is None:
                    raise WaterError("Cannot water None plant")
                print(f"Watering {plant} - success")
        except WaterError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")
    
    def check_plant_health(self, plant_name: str, water: int, sun: int) -> None:
        """Check if plant health parameters are valid"""
        try:
            if water < 1:
                raise WaterError(f"Water level {water} is too low (min 1)")
            elif water > 10:
                raise WaterError(f"Water level {water} is too high (max 10)")
            elif sun < 2:
                raise ValueError(f"Sunlight hours {sun} is too low (min 2)")
            elif sun > 12:
                raise ValueError(f"Sunlight hours {sun} is too high (max 12)")
            else:
                print(f"{plant_name}: healthy (water: {water}, sun: {sun})")
        except (WaterError, ValueError) as e:
            print(f"Error checking {plant_name}: {e}")
    
    def test_recovery(self) -> None:
        """Test error recovery"""
        try:
            raise GardenError("Not enough water in tank")
        except GardenError as e:
            print(f"Caught GardenError: {e}")
            print("System recovered and continuing...")


def test_garden_management() -> None:
    """Test the garden management system"""
    print("=== Garden Management System ===\n")
    
    garden_manager = GardenManager()
    
    print("Adding plants to garden...")
    garden_manager.add_plant("tomato")
    garden_manager.add_plant("lettuce")
    garden_manager.add_plant("")
    print()
    
    print("Watering plants...")
    garden_manager.water_plants()
    print()
    
    print("Checking plant health...")
    garden_manager.check_plant_health("tomato", 5, 8)
    garden_manager.check_plant_health("lettuce", 15, 8)
    print()
    
    print("Testing error recovery...")
    garden_manager.test_recovery()
    print()
    
    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
