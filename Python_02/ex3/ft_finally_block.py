def  water_plants(plant_list: list):
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None or plant == "":
                raise ValueError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    """Demonstrate finally block with both success and error cases"""
    
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
