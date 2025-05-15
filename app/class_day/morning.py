from app.manager_day.manager import DayManager

class Morning(DayManager):
    def __init__(self):
        self.period = "morning"
        self.dishes = ["eggs", "toast", "coffee", "error"]
        super().__init__(period=self.period, dishes=self.dishes)
