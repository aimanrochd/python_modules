class GardenError(Exception):
    """Base exception for garden-related problems"""
    pass


class PlantError(GardenError):
    """Exception for plant-specific problems"""
    pass


class WaterError(GardenError):
    """Exception for watering-related problems"""
    pass


def test_plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def test_water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")
    try:
        print("Testing PlantError...")
        test_plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")
    try:
        print("Testing WaterError...")
        test_water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")
    print("Testing catching all garden errors...")
    try:
        test_plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        test_water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")
    print("All custom error types work correctly!")


if __name__ == "__main__":
    try:
        test_custom_errors()
    except Exception as e:
        print(f"Error: {e}")
