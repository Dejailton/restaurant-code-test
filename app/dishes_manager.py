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
        if len(input_list) == 0:
            return ""
    
    def menu_return(self, menu: object, input_list: List[str]) -> str:
        list_menu = []
        menu_items = menu.get_menu()
        menu_length = self.get_length(menu)
        input_list_lenght = self.get_length(input_list)
        if input_list_lenght < 0 or input_list_lenght > menu_length:
            list_menu.append("error")
            
        for i in input_list:
            if i in menu_items[i]:
                list_menu.append(menu_items[i])
                
    def get_order_items(self, input: str) -> str:
        input_list = self.formatting(input)
        period = self.get_period()
        dishes = self.verification_period(period)
        output = self.verification_if_have_inputs(input_list)
        if output == "":
            return output
        dishes = dishes.menu_return(dishes, input_list)
        
        
        

        
        
        
    
