def handle_crisis(filename: str) -> None:
    print(f"CRISIS ALERT: Attempting access to '{filename}'...")
    try:
        with open(filename, 'r') as vault:
            vault.read()
            print("SUCCESS: Archive recovered. ''Knowledge preserved "
                  "for humanity''")
            print("STATUS: Normal operations resumed\n")
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable\n")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained\n")
    except Exception:
        print("RESPONSE: Unexpected system anomaly")
        print("STATUS: Crisis handled, system isolated\n")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    handle_crisis('lost_archive.txt')

    handle_crisis('classified_vault.txt')

    handle_crisis('standard_archive.txt')

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
