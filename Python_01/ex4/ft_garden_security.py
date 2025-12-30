class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self) -> int:
        return self._height
    
    def get_age(self) -> None:
        return self._age

    def set_height(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        if value < 0:
            print(f"Invalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days [OK]\n")


def main():
    print("=== Garden Security System ===")
    
    garden_rose = SecurePlant("Rose", 10, 30)
    print(f"Plant created: {garden_rose.name}")
    
    garden_rose.set_height(2)
    garden_rose.set_age(2)
    
    garden_rose.set_height(55)
    
    print(f"Current plant: {garden_rose.name} ({garden_rose.get_height()}cm, {garden_rose.get_age()} days)")


if __name__ == "__main__":
    main()