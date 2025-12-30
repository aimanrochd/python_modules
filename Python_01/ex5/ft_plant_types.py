class SecurePlant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self._height = height
        self._age = age

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

    def grow(self):
        self.set_height(self.get_height() + 1)


class Flower(SecurePlant):
    "It demonstrates Inheritance by allowing"
    "specialized classes like Flower and Tree"
    "to reuse the security logic of a Parent class"
    ", and Polymorphism by allowing each plant type"
    "to define its own unique growth behavior while"
    "still following the parent's rules."
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def grow(self):
        self.set_height(self.get_height() + 2)
        print(f"{self.name}'s color  is {self.color}")


class Tree(SecurePlant):
    def __init__(self, name, height, age, is_evergreen):
        super().__init__(name, height, age)
        self.is_evergreen = is_evergreen

    def grow(self):
        self.set_height(self.get_height() + 5)


def main():
    print("=== Garden Specialization System ===")

    # Create the specialized plants
    sunflower = Flower("Sunflower", 10, 5, "Yellow")
    pine = Tree("Pine", 50, 20, True)

    # Show they inherited the parent's attributes
    print(f"Created a {sunflower.color} {sunflower.name}")

    # Test different growth rates
    sunflower.grow()
    pine.grow()

    print(f"Sunflower height: {sunflower.get_height()}cm")
    print(f"Pine height: {pine.get_height()}cm")


if __name__ == "__main__":
    main()
