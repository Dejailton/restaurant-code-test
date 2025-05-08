from app.dishes.common import CommonDishes
from app.dishes.morning import MorningDishes
from app.dishes.night import NightDishes

class DishesManager:
    def __init__(self):
        self._dishes:list[CommonDishes] = [MorningDishes(), NightDishes()]      
      
    def process_order(self, input: str) -> str:
        if input is None or input == '':
            return "error"
        
        input = input.replace(" ", "")
        input = input.lower()
        input_list = input.split(",")        
        period: str = input_list.pop(0)
        
        dish = next((dish for dish in self._dishes if dish.get_period() == period), None)
        
        if dish is None:
            return "error"
        
        if len(input_list) == 0:
            return ''
        
        return dish.process_order(input_list)