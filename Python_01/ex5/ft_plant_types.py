class Plant:
    '''The Base Class That Has The Basic Plant Attributes'''
    def __init__(self, name: str, height: int, age: int) -> None:
        """Initializes the Plant with the necessary attributes."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> str:
        """a method to get basic infos about a plant"""
        return f"{self.height}cm, {self.age} days"

    def perform_action(self) -> None:
        """A default action if a specific one isn't defined."""
        print(f"{self.name} is photosynthesizing...")


class Flower(Plant):
    '''The First Derived Class Of Flower Type'''
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initializes the Flower with the necessary attributes."""
        super().__init__(name, height, age)
        self.color = color

    def get_info(self) -> str:
        """a method to get infos about a Flower Plant"""
        basic_stats = super().get_info()
        return f"{self.name} (Flower): {basic_stats}, {self.color} color"

    def bloom(self) -> None:
        """a method for Flower plant to bloom"""
        print(f"{self.name} is blooming beautifully!")

    def perform_action(self) -> None:
        """a method that perform the action"""
        self.bloom()


class Tree(Plant):
    '''The Second Derived Class Of Tree Type'''
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initializes the Tree with the necessary attributes."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> str:
        """a method to get infos about a Tree"""
        basic_stats = super().get_info()
        return (f"{self.name} (Tree): {basic_stats}, "
                f"{self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        """a method for tree to produce the shade"""
        shade = (self.height // self.trunk_diameter) + 68
        print(f"{self.name} provides {shade} square meters of shade")

    def perform_action(self) -> None:
        """a method that perform the action"""
        self.produce_shade()


class Vegetable(Plant):
    """The Third Derived Class Of Vegetable Type"""
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initializes the Vegetable with the necessary attributes."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> str:
        """a method to get infos about Vegetbles"""
        basic_stats = super().get_info()
        return (f"{self.name} (Vegetable): {basic_stats},"
                f" {self.harvest_season} harvest")

    def perform_action(self) -> None:
        """a method to show the nutritional value in a Vegetable"""
        print(f"{self.name} is {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    garden_plants = [
        Flower("Rose", 25, 30, "red"),
        Flower("SunFlower", 80, 45, "yellow"),

        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 400, 1095, 40),

        Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C"),
        Vegetable("Carrot", 30, 75, "autumn", "rich in vitamin D")
    ]
    first = True
    for plant in garden_plants:
        if not first:
            print()
        first = False
        print(plant.get_info())
        plant.perform_action()
