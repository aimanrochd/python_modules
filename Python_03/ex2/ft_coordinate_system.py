import math


def create_position(coordinates: tuple) -> tuple:
    """"""
    x, y, z = coordinates
    if x or y or z != 0:
        print(f"Position created: {coordinates}")
    return coordinates


def distance_calculator(pos: tuple) -> float:
    """"""
    coordinates: tuple = 0, 0, 0
    base_pos = create_position(coordinates)
    distance = math.sqrt((pos[0] - base_pos[0])**2 +
                         (pos[1] - base_pos[1])**2 + (pos[2] - base_pos[2])**2)
    print(f"Distance between (0, 0, 0) and {pos}: ", end="")
    return distance


def parsing(coordinates: str):
    """"""
    try:
        str_coordinates_list = coordinates.split(',')
        int_coordinates_list = []
        for i in str_coordinates_list:
            int_coordinates_list += [int(i.strip())]

        parsed_position = tuple(int_coordinates_list)

        print(f"Parsing coordinates: \"{coordinates}\"")
        print(f"Parsed position: {parsed_position}")
        return parsed_position

    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coordinates}\"")
        print(f"Error parsing coordinates: {e}")
        print(f'Error details - Type: {type(e).__name__}, Args: ("{e}",)\n')
        return None


def unpacking_dem(position: tuple):
    """"""
    print("Unpacking demonstration:")
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={position[0]}, Y={position[1]}, Z={position[2]}")


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")

    invalid_input = "abc,def,ghi"
    coordinates: tuple = 10, 20, 5
    pos = create_position(coordinates)

    distance = distance_calculator(pos)
    print(f"{distance:.2f}\n")

    parsed_position = parsing("3,4,0")
    distance_2 = distance_calculator(parsed_position)
    print(f"{distance_2:.1f}\n")

    parsing(invalid_input)

    unpacking_dem(parsed_position)
