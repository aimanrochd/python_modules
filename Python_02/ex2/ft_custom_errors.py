class GardenError(Exception):
    """Base class for garden-related errors"""
    pass


class PlantError(GardenError):
    """Exception for plant-related problems"""
    pass


class WaterError(GardenError):
    """Exception for water-related problems"""
    pass


def check_plant(plant_name: str):
    """Check plant health - raises PlantError if plant is wilting"""
    if plant_name == "tomato":
        raise PlantError("The tomato plant is wilting!")
    print(f"{plant_name} is healthy!")


def check_water(tank_level: int):
    """Check water tank - raises WaterError if low"""
    if tank_level < 20:
        raise WaterError("Not enough water in the tank!")
    print(f"Water tank level: {tank_level}%")


def test_custom_errors():
    """Demonstrate custom exception types"""
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        check_plant("tomato")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print()

    print("Testing WaterError...")
    try:
        check_water(10)
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print()

    print("Testing catching all garden errors...")
    try:
        check_plant("tomato")
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        check_water(5)
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
