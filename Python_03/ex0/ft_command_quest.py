import sys


def ft_command_quest() -> None:
    program_name = sys.argv[0]
    total_args = len(sys.argv)
    arguments = sys.argv[1:]

    print("=== Command Quest ===")
    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {total_args}")

    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {total_args - 1}")
        i = 1
        for arg in arguments:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    try:
        ft_command_quest()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
