import math


def create_position(coordinates: tuple) -> tuple:
    print(f"Position created: {coordinates}")
    return coordinates


def distance_calculator(target_pos: tuple, base_pos:
                        tuple = (0, 0, 0)) -> float | None:
    try:
        x1, y1, z1 = target_pos

        x2, y2, z2 = base_pos

        distance = math.sqrt(
            (x2 - x1)**2 +
            (y2 - y1)**2 +
            (z2 - z1)**2
        )

        print(f"Distance between {base_pos} and {target_pos}: ", end="")
        return distance

    except ValueError:
        print(f"Error: Invalid position format. "
              f"Got {target_pos} and {base_pos}")
        return None


def parsing(coordinates: str) -> tuple | None:
    try:
        parts = coordinates.split(',')
        p1, p2, p3 = parts
        parsed_position = (int(p1), int(p2), int(p3))
        print(f"Parsing coordinates: \"{coordinates}\"")
        print(f"Parsed position: {parsed_position}")
        return parsed_position
    except ValueError as e:
        error_type = e.__class__.__name__
        error_args = e.args
        print(f"Parsing invalid coordinates: \"{coordinates}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {error_type}, Args: {error_args}")
        return None


def unpacking_dem(position: tuple) -> None:
    print("Unpacking demonstration:")
    try:
        x, y, z = position
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")
    except ValueError:
        print("Error: Position does not contain exactly 3 coordinates.")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    coordinates = (10, 20, 5)
    pos = create_position(coordinates)

    dist = distance_calculator(pos)
    if dist is not None:
        print(f"{dist:.2f}\n")

    parsed_pos = parsing("3,4,0")
    if parsed_pos:
        dist_2 = distance_calculator(parsed_pos)
        if dist_2 is not None:
            print(f"{dist_2:.1f}\n")

        parsing("abc,def,ghi")
        print()
        unpacking_dem(parsed_pos)


if __name__ == "__main__":
    main()
