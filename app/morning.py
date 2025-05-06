class Morning:
    def __init__(self):
        self.day = "morning"
        self.entree = "eggs"
        self.side = "toast"
        self.drink = "coffee"
        self.dessert = "Not_Applicable"
        
    def get_day(self) -> str:
        return self.day
    
    def get_entree(self) -> str:
        return self.entree

    def get_side(self) -> str:
        return self.side
    
    def get_drink(self) -> str:
        return self.drink
    
    def get_dessert(self) -> str:
        self.dessert = "error"
        return self.dessert
