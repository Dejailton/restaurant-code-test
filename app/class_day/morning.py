from app.manager_day.manager import DayManager

class Morning(DayManager):
    def __init__(self):
        self.period = "morning"
        self.dishes = ["eggs", "toast", "coffee"]
        super().__init__(period=period, dishes=dishes)