from .dishes.morning import MorningDishes
from .dishes.night import NightDishes


class DishTable:
    def __init__(self, period: str):  
        self._period = period      
        self._dishes = [MorningDishes(), NightDishes()]        
        
    def get_period(self) -> str:
        return self._period.lower()
    
    def get_items(self, input: str) -> str: 
        for dish in self._dishes:
            if dish.get_period() == self._period.lower():
                return dish.get_items(input)                  
    