class Night:
    def __init__(self):
        self.day = "night"
        self.entree = "steak"
        self.side = "potato"
        self.drink = "wine"
        self.dessert = "cake"
        
    def get_day(self) -> str:
        return self.day
        
    def get_entree(self) -> str:
        return self.entree

    def get_side(self) -> str:
        return self.side
    
    def get_drink(self) -> str:
        return self.drink
    
    def get_dessert(self) -> str:
        return self.dessert
    
    def get_error(self) -> str:
        return "error"