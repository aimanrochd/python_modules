import alchemy

def main() -> None:
    print('=== Sacred Scroll Mastery ===\n')

    print('Testing direct module access:')
    print(f'alchemy.elements.create_fire(): {alchemy.elements.create_fire()}')
    print(f'alchemy.elements.create_water(): {alchemy.elements.create_water()}')
    print(f'alchemy.elements.create_earth(): {alchemy.elements.create_earth()}')
    print(f'alchemy.elements.create_air(): {alchemy.elements.create_air()}\n')

    print('Testing package-level access (controlled by __init__.py):')

    tests = [
        ("create_fire",  lambda: alchemy.create_fire()),
        ("create_water", lambda: alchemy.create_water()),
        ("create_earth", lambda: alchemy.create_earth()),
        ("create_air",   lambda: alchemy.create_air()),
    ]

    for name, action in tests:
        try:
            print(f'alchemy.{name}(): {action()}')
        except AttributeError:
            print(f'alchemy.{name}(): AttributeError - not exposed')

    print('\nPackage metadata:')
    print(f'Version: {alchemy.__version__}')
    print(f'Author: {alchemy.__author__}')

if __name__ == "__main__":
    main()
