from app.manager_day.manager import DayManager

class Morning(DayManager):
    def __init__(self):
        self.period = "morning"
        self.dishes = ["eggs", "toast", "coffee", "error"]
        self.repetitive_dish = ["coffee", "3"]
        super().__init__(period=self.period, dishes=self.dishes, repetitive_dish=self.repetitive_dish)