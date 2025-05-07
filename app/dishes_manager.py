from app.dishes.morning import MorningDishes
from app.dishes.night import NightDishes

class DishesManager:
    def __init__(self):
        self._dishes = [MorningDishes(), NightDishes()]      
      
    def process_order(self, input: str) -> str:
        if input == '':
            return "error"
        
        input = input.replace(" ", "")
        input_list = input.split(",")
        
        period: str = input_list[0].lower()
        input_list.pop(0)
        input_list.sort()
        
        for dish in self._dishes:
            if dish.get_period() == period:
                return dish.process_order(input_list)
        
        return "error"
    