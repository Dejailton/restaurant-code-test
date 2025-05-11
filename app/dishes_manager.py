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
    def menu_selection(self, input: List[str]) -> List[str]:
        period = input[0]
        day = self.verify_period(period)
        count = 0
        day_class = day
        day = day.get_dishes()
        input = self.list_order(input)
        for dish in input:
            dishe = day[int(dish)-1]
            if period == "morning" and dish == "3":
                count += 1
                if count > 1:
                    repeat = day_class.dishe_sum_autorized(input, period, day_class)
                    self.dishes.clear()
                    self.dishes.extend(repeat)
                    break
            elif period == "night" and dish == "2":
                count += 1
                if count > 1:
                    repeat = day_class.dishe_sum_autorized(input, period, day_class)
                    self.dishes.clear()
                    self.dishes.extend(repeat)
                    break
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