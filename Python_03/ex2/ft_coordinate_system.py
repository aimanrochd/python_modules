# NOT READY IT STILL HAS SOME ERRORS (FLOATING POINTS IN THE COORDINATES ......)
import math
# import sys


def create_position(coordinates: tuple) -> tuple:
    print(f"Position created: {coordinates}")
    return coordinates


def distance_calculator(pos: tuple) -> float:

    base_x, base_y, base_z = 0, 0, 0
    pos_x, pos_y, pos_z = pos

    distance = math.sqrt(
        (pos_x - base_x)**2 +
        (pos_y - base_y)**2 +
        (pos_z - base_z)**2
    )
    print(f"Distance between (0, 0, 0) and {pos}: ", end="")
    return distance


def parsing(coordinates: str) -> tuple | None:
    try:
        parts = coordinates.split(',')

        p1, p2, p3 = parts

        parsed_position = (int(p1), int(p2), int(p3))

        print(f"Parsing coordinates: \"{coordinates}\"")
        print(f"Parsed position: {parsed_position}")
        return parsed_position

    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coordinates}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details Type: {type(e).__name__}, Args: {e.args}")
        return None


def unpacking_dem(position: tuple) -> None:
    print("Unpacking demonstration:")
    try:
        x, y, z = position
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError:
        print("Error: Position does not contain exactly 3 coordinates.")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    coordinates = (10, 20, 5)
    pos = create_position(coordinates)

    distance = distance_calculator(pos)
    print(f"{distance:.2f}\n")

    parsed_position = parsing("3,4,0")
    if parsed_position:
        distance_2 = distance_calculator(parsed_position)
        print(f"{distance_2:.1f}\n")

        unpacking_dem(parsed_position)

    parsing("abc,def,ghi")

    print("\n--- Testing Dimension Error (Unpacking Check) ---")
    parsing("1,2")
