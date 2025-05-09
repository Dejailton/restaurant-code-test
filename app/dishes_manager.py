from .class_day.morning import Morning
from .util.formatter import Formatter

class DishesManager(Formatter):
    def __init__(self):
        self.dishes = {}
    
    def manager_output(self, input:str) -> str:
        match input:
                case "morning":
                    return ""
                case "night":
                    return ""
                case _:
                    return "error"
                
    def process_order(self, input: str):
        input = self.format_lower(input)
        output = self.manager_output(input)
        return output