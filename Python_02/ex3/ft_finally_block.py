def water_plants(plant_list: list) -> None:
    """
    Waters plants from the list and ensures cleanup happens
    """
    try:
        print("Opening watering system")

        for plant in plant_list:
            if plant is None:
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Demonstrates finally block with normal and error cases"""
    try:
        print("=== Garden Watering System ===\n")

        print("Testing normal watering...")
        water_plants(["tomato", "lettuce", "carrots"])
        print("Watering completed successfully!\n")

        print("Testing with error...")
        water_plants(["tomato", None, "carrots"])
        print("\nCleanup always happens, even with errors!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_watering_system()
