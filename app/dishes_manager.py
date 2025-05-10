from typing import List
from app.class_day.night import Night
from .class_day.morning import Morning
from .util.formatter import Formatter

class DishesManager(Formatter):
    def __init__(self):
        self.dishes = []
        
    def verify_period(self, input: str):
        if input[0] == "morning":
            return Morning()
        elif input[0] == "night":
            return Night()
    def menu_selection(self, input: List[str]) -> List[str]:
        day = self.verify_period(input)
        day = day.get_dishes()
        input = self.list_order(input)
        for dish in input:
            dishe = day[int(dish)-1]
            self.dishes.append(dishe)
    def manager_output(self, input:str) -> str:
        if len(input) == 1:
            match input:
                    case ["morning"]:
                        return ""
                    case ["night"]:
                        return ""
                    case _:
                        return "error"
        elif len(input) >= 2:
            self.menu_selection(input)
        else:
            return "error"    
    def process_order(self, input: str):
        input = self.format_lower(input)
        list = self.format_list(input)
        output = self.manager_output(list)
        if len(list) <= 1 or output == "error":
            if list[0] == "1":
                return self.format_output(self.dishes)
            return output
        elif len(input) >= 2:
            output = self.format_output(self.dishes)
            return output