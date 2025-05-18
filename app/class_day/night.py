from app.manager_day.manager import DayManager

class Night(DayManager):
    def __init__(self):
        self.period = "night"
        self.dishes = ["steak", "potato", "wine", "cake"]
        self.repetitive_dish = ["potato", "2"]
        super().__init__(period=self.period, dishes=self.dishes, repetitive_dish=self.repetitive_dish)
        
    