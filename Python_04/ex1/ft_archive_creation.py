def create_archive(filename: str) -> None:
    print(f"Initializing new storage unit: {filename}")

    file = open(filename, 'w')
    print("Storage unit created successfully...")

    print("\nInscribing preservation data...")
    entry1 = "[ENTRY 001] New quantum algorithm discovered"
    file.write(entry1 + '\n')
    print(entry1)

    entry2 = "[ENTRY 002] Efficiency increased by 347%"
    file.write(entry2 + '\n')
    print(entry2)

    entry3 = "[ENTRY 003] Archived by Data Archivist trainee"
    file.write(entry3 + '\n')
    print(entry3)

    print()
    file.close()

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_archive('new_discovery.txt')
