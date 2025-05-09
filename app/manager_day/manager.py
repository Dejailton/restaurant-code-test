class DayManager:
    def __init__(self, period, dishes):
        self._day = period
        self._dishes = dishes

    def get_day(self):
        return self._day
    
    def get_dishes(self):
        return self._dishes