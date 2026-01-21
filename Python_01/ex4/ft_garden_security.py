class SecurePlant:
    """A secure plant implementation that validates height and age
    to prevent corruption."""
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the plant with a name, height and age"""
        self.name = name
        print(f"Plant created: {self.name}")
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """a method to get the height"""
        return self.__height

    def get_age(self) -> int:
        """a method to get the age"""
        return self.__age

    def set_height(self, value: int) -> None:
        """a method to set the height with some conditions"""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {value}cm [OK]")

    def set_age(self, value: int) -> None:
        """a method to set the age with some conditions"""

        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {value} days [OK]")

    def get_info(self) -> None:
        """a method that print some infos about the plant"""
        print(f"Current plant: {self.name} ({self.get_height()}cm, "
              f"{self.get_age()} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")

    rose = SecurePlant("Rose", 25, 30)
    print()
    rose.set_height(-5)
    print()
    rose.get_info()
