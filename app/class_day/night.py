from app.manager_day.manager import DayManager

class Night(DayManager):
    def __init__(self):
        self.period = "night"
        self.dishes = ["steak", "potato", "wine", "cake"]
        super().__init__(period=self.period, dishes=self.dishes)
        
    