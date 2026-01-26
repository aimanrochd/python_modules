def garden_operations(error: object) -> None:
    """Demonstrates different types of errors that can occur"""

    if error is ValueError:
        int("abc")
    elif error is ZeroDivisionError:
        10 / 0
    elif error is FileNotFoundError:
        open("missing.txt", "r")
    elif error is KeyError:
        plants = {"plant": "rose", "age": 45}
        plants['missing_plant']


def test_error_types():
    """a function that shows each type of error happening"""
    try:
        print("=== Garden Error Types Demo ===\n")
        try:
            print("Testing ValueError...")
            garden_operations(ValueError)
        except ValueError as e:
            print(f"Caught ValueError: {e}\n")
        try:
            print("Testing ZeroDivisionError...")
            garden_operations(ZeroDivisionError)
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}\n")
        try:
            print("Testing FileNotFound...")
            garden_operations(FileNotFoundError)
        except FileNotFoundError as e:
            print(f"Caught FileNotFound: {e}\n")
        try:
            print("Testing KeyError...")
            garden_operations(KeyError)
        except KeyError as e:
            print(f"Caught KeyError: {e}\n")
        try:
            print("Testing multiple errors together...")
            garden_operations(ValueError)
        except (ValueError, ZeroDivisionError, KeyError):
            print("Caught an error, but program continues!\n")
        print("All error types tested successfully!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    test_error_types()
