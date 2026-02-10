def create_archive(filename: str) -> None:
    print(f"Initializing new storage unit: {filename}")
    
    file = open(filename, 'w')
    print("Storage unit created successfully...")
    print("\nInscribing preservation data...")

    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    print("[ENTRY 002] Efficiency increased by 347%")
    
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("[ENTRY 003] Archived by Data Archivist trainee\n")

    file.close()
    
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    create_archive('new_discovery.txt')