# CODE DONE
import sys


def ft_command_quest() -> None:
    program_name = sys.argv[0]
    args_nbr = len(sys.argv)
    arguments = sys.argv[1:]

    print("=== Command Quest ===")
    if args_nbr == 1:
        print("No arguments provided!")
        print(f"Program name: {program_name}")
        print(f"Total arguments: {args_nbr}")

    else:
        print(f"Program name: {program_name}")
        print(f"Arguments received: {args_nbr - 1}")
        i = 1
        for arg in arguments:
            print(f"Argument {i}: {arg}")
            i += 1
        print(f"Total arguments: {args_nbr}")


if __name__ == "__main__":
    ft_command_quest()
