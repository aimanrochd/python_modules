def recover_ancient_text(filename: str) -> None:

    file = open(filename, 'r')
    content = file.read()

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")
    print("Connection established...\n")
    print("RECOVERED DATA:")
    print(content)
    print("\nData recovery complete. Storage unit disconnected.")
    file.close()


if __name__ == "__main__":
    recover_ancient_text("ancient_fragment.txt")
