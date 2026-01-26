def check_temperature(temp_str: str) -> int | None:
    try:
        temp = int(temp_str)
    except Exception:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    try:
        if (temp <= 40 and temp >= 0):
            print(f"Temperature {temp}°C is perfect for plants!")
            return temp
        elif temp > 40:
            raise ValueError(f"Error: {temp}°C is too"
                             f"hot for plants (max 40°C)")
        elif temp < 0:
            raise ValueError(f"Error: {temp}°C is too cold "
                             f"for plants (min 0°C)")
    except Exception as e:
        print(f"Error: {e}")
        return None


def test_temperature_input():
    try:
        print("=== Garden Temperature Checker ===\n")

        test_cases = ["25", "abc", "100", "-50"]

        for value in test_cases:
            print(f"Testing temperature: {value}")
            check_temperature(value)
            print()

        print("All tests completed - program didn't crash!")
    except Exception as e:
        print(f"Error: {e}\n")


if __name__ == "__main__":
    test_temperature_input()
