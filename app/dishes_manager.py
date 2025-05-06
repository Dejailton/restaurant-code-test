from .dishes.morning import MorningDishes
from .dishes.night import NightDishes


class DishesManager:
    def __init__(self):          
        self._dishes = [MorningDishes(), NightDishes()]        
        
    def get_period(self) -> str:
        return self._period.lower()
    
    def get_order_items(self, input: str) -> str:
        input = input.replace(" ", "")
        input_list = input.split(",")
        
        if len(input_list) == 0:
            return "error"
        
        period: str = input_list[0].lower()
        input_list.pop(0)
        input_list.sort()
        
        for dish in self._dishes:
            if dish.get_period() == period:
                return dish.get_order_items(input_list)
        
        return "error"
    