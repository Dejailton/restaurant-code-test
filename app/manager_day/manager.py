class DayManager:
    def __init__(self, period, dishes):
        self._day = period
        self._dishes = dishes

    def get_day(self):
        return self.day