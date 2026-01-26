def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    if sunlight_hours > 12:
        raise ValueError(f" Sunlight hours {sunlight_hours} is "
                         f"too hight (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks():
    try:
        print("=== Garden Plant Health Checker ===\n")
        print("Testing good values...")
        try:
            result = check_plant_health("tomato", 5, 8)
            print(f"{result}\n")
        except ValueError as e:
            print(f"Error: {e}\n")
        print("Testing empty plant name...")
        try:
            check_plant_health("", 5, 8)
        except ValueError as e:
            print(f"Error: {e}\n")
        print("Testing bad water level...")
        try:
            check_plant_health("tomato", 15, 8)
        except ValueError as e:
            print(f"Error: {e}\n")
        print("Testing bad sunlight hours...")
        try:
            check_plant_health("tomato", 5, 0)
        except ValueError as e:
            print(f"Error: {e}\n")
        print("All error raising tests completed!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_plant_checks()
