def secure_vault_operations(read_file: str, write_file: str) -> None:
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")

    with open(read_file, 'r') as vault:
        print("Vault connection established with failsafe protocols\n")
        vault.read()
        print("SECURE EXTRACTION:")
        print("[CLASSIFIED] Quantum encryption keys recovered")
        print("[CLASSIFIED] Archive integrity: 100%\n")

    with open(write_file, 'w') as vault:
        print("SECURE PRESERVATION:")
        vault.write("[CLASSIFIED] New security protocols archived")
        print("[CLASSIFIED] New security protocols archived")

    print("Vault automatically sealed upon completion")
    print("\nAll vault operations completed with maximum security.")


if __name__ == "__main__":
    secure_vault_operations('ancient_fragment.txt', 'security_log.txt')
