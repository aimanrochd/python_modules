import sys


def manage_streams() -> None:
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n",
          file=sys.stdout)

    arch_id: str = input("Input Stream active. Enter archivist ID: ")
    status: str = input("Input Stream active. Enter status report: ")

    print(f"\n[STANDARD] Archive status from {arch_id}: {status}",
          file=sys.stdout)

    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)

    print("[STANDARD] Data transmission complete",
          file=sys.stdout)
    print("\nThree-channel communication test successful.",
          file=sys.stdout)


if __name__ == "__main__":
    manage_streams()
