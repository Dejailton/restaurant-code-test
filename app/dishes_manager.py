from typing import List
from .class_day.night import Night
from .class_day.morning import Morning
from .util.formatter import Formatter

class DishesManager(Formatter):
    def __init__(self):
        self.dishes = []
        
    def verify_period(self, period: str):
        if period == "morning":
            return Morning()
        elif period == "night":
            return Night()
        
    def menu_selection(self, inputs) -> None:
        period = inputs[0]
        day = self.verify_period(period)
        count = 0
        dishes_on_the_menu = day.get_dishes()
        inputs_order = self.list_order(inputs)
        repetitive_dish = day.get_repetitive_dish()
        for dish in inputs_order:
            verify_dish = day.dish_verify(self.dishes, dishes_on_the_menu, dish)
            
            if verify_dish:
                self.dishes.append("error")
                break
            
            if dish == repetitive_dish[1]:
                count += 1
            
            if count > 1:
                dishes = day.get_output_autorized(inputs, repetitive_dish)
                self.dishes.clear()
                self.dishes.extend(dishes)
                break
            
            get_dish = dishes_on_the_menu[int(dish)-1]
            self.dishes.append(get_dish)
            
    def manager_output(self, inputs:str) -> str:
        if len(inputs) == 1:
            match inputs:
                    case ["morning"]:
                        return ""
                    case ["night"]:
                        return ""
                    case _:
                        return "error"
        elif len(inputs) >= 2:
            self.menu_selection(inputs)
            
    def process_order(self, inputs: str) -> str:
        input_lower = self.format_lower(inputs)
        input_list = self.format_list(input_lower)
        output = self.manager_output(input_list)
        if output == "error":
            return output
        else:
            output = self.format_output(self.dishes)
            return output