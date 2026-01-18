class Plant:
    def __init__(self, name, height):
        self.name = name
        self._height = height
    def grow(self, amount) -> None:
        self._height += amount
        print(f"the plant grow by {amount}cm")
    def get_height(self) -> None:
        return(self._height)

class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color
        self.is_blooming = False
    def bloom(self):
        self.is_blooming = True
    def get_info(self):
        return f"{self.name}: {self._height}cm, {self.flower_color} flowers ({'blooming' if self._is_blooming else 'not blooming'})"

class PrizeFlower(FloweringPlant):
        def __init__(self, name, height, flower_color, prize_points):
            super().__init__(name, height, flower_color)
            self.prize_points = prize_points
        def get_info(self):
            base_info = super().get_info()
            return f"{base_info}, Prize points: {self.prize_points}"



class GardenManager:
    gardens = {}
    
    class GardenStats:
        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0
        
        def record_plant(self, plant):
            self.plants_added += 1
            if plant == 'PrizeFlower':
                self.prize_flowers += 1
            elif plant == 'FloweringPlant':
                self.flowering_plants += 1
            elif plant == 'Plant':
                self.regular_plants += 1
        
        def record_growth(self, amount=1):
            self.total_growth += amount
        
        def get_report(self):
            return (f"Plants added: {self.plants_added}, "
            f"Total growth: {self.total_growth}cm\n"
            f"Plant types: {self.regular_plants} regular, "
            f"{self.flowering_plants} flowering, "
            f"{self.prize_flowers} prize flowers")
    
    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.gardens[owner_name] = self
    
    def add_plant(self, plant : Plant):
        