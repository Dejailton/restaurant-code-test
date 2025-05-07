from .dishes.morning import MorningDishes
from .dishes.night import NightDishes
from .utils.formatter import Formatter


class DishesManager(Formatter):
    def __init__(self):          
        self._dishes = [MorningDishes(), NightDishes()]   
        
    def verification_period(self, period: str) -> object:
        if period == "morning":
            return MorningDishes()
        elif period == "night":
            return NightDishes()
        
    def verification_if_have_inputs(self, input_list: list) -> str:
        if len(input_list) == 0:
            return ""
        
    def get_order_items(self, input: str) -> str:
        input_list = self.formatting(input)
        period = self.get_period()
        dishes = self.verification_period(period)
        output = self.verification_if_have_inputs(input_list)
        if output == "":
            return output
        
        
        
        

        
        
        
    
