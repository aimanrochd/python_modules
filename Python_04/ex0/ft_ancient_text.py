def recover_ancient_text(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")

    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return

    print(f"Accessing Storage Vault: {filename}")
    print("Connection established...\n")

    content = file.read()

    print("RECOVERED DATA:")
    print(content)

    print("\nData recovery complete. Storage unit disconnected.")
    file.close()


if __name__ == "__main__":
    recover_ancient_text("ancient_fragment.txt")
