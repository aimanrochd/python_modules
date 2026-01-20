def check_temperature(temp_str: str):
    try:
        temp = int(temp_str)
    except (ValueError, TypeError):
        raise ValueError(f"Error: '{temp_str}' is not a valid number")

    if temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")

    return temp


def test_temperature_input():
    sensor_readings = ["25", "abc", "100", "-50"]

    print("=== Garden Temperature Checker ===\n")

    for reading in sensor_readings:
        print(f"Testing temperature: {reading}")
        try:
            valid_temp = check_temperature(reading)
            print(f"Temperature {valid_temp}°C is perfect for plants!")
            print()

        except ValueError as error:
            print(error)
            print()

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
