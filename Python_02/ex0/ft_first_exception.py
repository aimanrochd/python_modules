def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if temp > 40:
        raise ValueError(f"Error: {temp}°C is too hot for plants (max 40°C)")
    elif temp < 0:
        raise ValueError(f"Error: {temp}°C is too cold for plants (min 0°C)")
    print(f"Temperature {temp}°C is perfect for plants!")
    return temp


def test_temperature_input() -> None:

    print("=== Garden Temperature Checker ===\n")
    test_cases = ["25", "abc", "100", "-50"]

    for value in test_cases:
        print(f"Testing temperature: {value}")
        try:
            check_temperature(value)
        except ValueError as e:
            print(e)
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    try:
        test_temperature_input()
    except Exception as e:
        print(f"Unexpected fatal error: {e}")
