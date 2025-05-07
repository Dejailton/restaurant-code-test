from typing import List


class CommonDishes:
    def __init__(self, period:str, menu:list):
        self._period = period
        self._menu = menu
        
    def get_period(self) -> str:
        return self._period