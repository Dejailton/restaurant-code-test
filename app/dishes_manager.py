from typing import List
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
        if len(input_list) == 1:
            return ""
    
    def menu_return(self, dishes: object, input_list: List[str]) -> str:
        list_formatter = self.formatter_index(input_list)
        list_menu = []
        menu_items = dishes.get_menu()
        menu_length = self.get_length(menu_items)
        input_list_lenght = self.get_length(input_list)
        
        
        if input_list_lenght < 0 or input_list_lenght > menu_length:
            list_menu.append("error")
        for i in list_formatter:
            list_menu.append(menu_items[i])
        
        return list_menu
                
    def get_order_items(self, input: str) -> str:
        input_list = self.formatting(input)
        period = self.get_period()
        dishes = self.verification_period(period)
        output = self.verification_if_have_inputs(input_list)
        if output == "":
            return output
        dishes = self.menu_return(dishes, input_list)
        dishes = self.convert_to_str(dishes)
        return dishes
        
        
        

        
        
        
    
