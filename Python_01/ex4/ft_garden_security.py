class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        print(f"Plant created: {self.name}")
        self._height = 0
        self._age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        return self._height
    
    def get_age(self) -> int:
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
    
    garden_rose = SecurePlant("Rose", 25, 30)
    
    garden_rose.set_height(-5)
    
    print(f"Current plant: {garden_rose.name} ({garden_rose.get_height()}cm, {garden_rose.get_age()} days)")


if __name__ == "__main__":
    main()