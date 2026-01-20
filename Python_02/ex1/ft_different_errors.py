def garden_operations():
    try:
        print('Testing ValueError...')
        _ = int('abc')
    except ValueError:
        print('Caught ValueError: invalid literal for int()')
    print()

    try:
        print('Testing ZeroDivisionError...')
        _ = 10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        print('Testing FileNotFoundError...')
        open('missing.txt')
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'")
    print()

    try:
        print('Testing KeyError...')
        dictionary = {"tomato": 10, "lettuce": 5}
        print(dictionary["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing_plant'")
    print()

    try:
        print('Testing multiple errors together...')
        operation = "divide"

        if operation == "divide":
            _ = 10 / 0
        elif operation == "convert":
            _ = int("abc")
    except (ValueError, ZeroDivisionError, FileNotFoundError):
        print("Caught an error, but program continues!")
    print()


def test_error_types():
    """Test function that runs all error demonstrations"""
    print("=== Garden Error Types Demo ===\n")

    garden_operations()

    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
