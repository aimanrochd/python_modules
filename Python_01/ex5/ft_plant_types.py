class Plant():
    '''The Base Class That Have The Basic Plant Attributes'''
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age
    def get_info(self):
        print("")

class Flower(Plant):
    '''The First Derived Class Of Flower Type With Color Attirbute'''
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
    def bloom(self):
        '''A Method To Print 'blooming' '''
        print(f"{self.name} is blooming beautifully!")
        
class Tree(Plant):
    '''The Second Derived Class Of Tree With trunk_diameter Attribute'''
    def __init__(self, name, height, age,  trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
    def produce_shade(self):
        '''A Method To Calculate And Print The Shade'''
        shade  = self.height / self.trunk_diameter + 68
        print(f"{self.name} provides {shade} square meters of shade")
        
class Vegetable(Plant):
    '''The Third Derived Class Of Vegetable Type With nutritional_value & harvest_season Attributes'''
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
    def get_info(self):
        '''A Method To Get nutritional_value Of A Vegetable'''
        print(f"{self.name} {self.nutritional_value}")
        
        
if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    rose = Flower("Rose", 25, 30, "red")
    sunflower = Flower("SunFlower", 80, 45, "yellow")
    
    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 400, 1095, 40)
    
    tomato = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    carrot = Vegetable("Carrot", 30, 75, "autumn", "rich in vitamin D")
    
    print(f"{rose.name} (Flower): {rose.height}cm, {rose.age} days, {rose.color} color")
    rose.bloom()
    print()
    
    print(f"{sunflower.name} (Flower): {sunflower.height}cm, {sunflower.age} days, {sunflower.color} color")
    sunflower.bloom()
    print()
    
    print(f"{oak.name} (Tree): {oak.height}cm, {oak.age} days, {oak.trunk_diameter}cm diameter")
    oak.produce_shade()
    print()
    
    print(f"{pine.name} (Tree): {pine.height}cm, {pine.age} days, {pine.trunk_diameter}cm diameter")
    pine.produce_shade()
    print()
    
    print(f"{tomato.name} (Vegetable): {tomato.height}cm, {tomato.age} days, {tomato.harvest_season} harvest")
    tomato.get_info()
    print()
    
    print(f"{carrot.name} (Vegetable): {carrot.height}cm, {carrot.age} days, {carrot.harvest_season} harvest")
    carrot.get_info()
