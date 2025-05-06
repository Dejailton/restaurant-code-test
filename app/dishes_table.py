from typing import List
from .morning import Morning
from .night import Night


class Dishes_Table(Morning, Night):
    def __init__(self):
        self.dish_type = ["day"]
        self.morning = Morning()
        self.night = Night()
        
    def return_dish_type(self):
        return self.dish_type
        
    def verification_time_of_day(self, input_list) -> None:
        self.dish_type[0] = input_list[0]
        if (self.dish_type[0] == "morning"):
            self.dish_type[0] = self.morning.get_day()
            self.return_dishes_morning(input_list)
            
        elif (self.dish_type[0] == "night"):
            self.dish_type[0] = self.night.get_day()
            self.return_dishes_night(input_list)
            
    def return_dishes_morning(self, input_list):
        if self.dish_type[0] == "morning":
            for i in input_list:
                match i:
                    case "1":
                        self.dish_type.append(self.morning.get_entree())
                    case "2":
                        self.dish_type.append(self.morning.get_side())
                    case "3":
                        self.dish_type.append(self.morning.get_drink())
                    case "4":
                        self.dish_type.append(self.morning.get_dessert())
                        
    def return_dishes_night(self, input_list):
        if self.dish_type[0] == "night":
            for i in input_list:
                match i:
                    case "1":
                        self.dish_type.append(self.night.get_entree())
                    case "2":
                        self.dish_type.append(self.night.get_side())
                    case "3":
                        self.dish_type.append(self.night.get_drink())
                    case "4":
                        self.dish_type.append(self.night.get_dessert())
                        
    def verification_quantity_request_dishes(self, input_list):
        entree = 0
        side = 0
        drink = 0
        dessert = 0
        for i in input_list:
            match i:
                case "1":
                    entree += 1
                case "2":
                    side += 1
                case "3":
                    drink += 1
                case "4":
                    dessert += 1
        return entree, side, drink, dessert
                    
    def conversion_to_list(self, input: str) -> List[str]:
        input = input.split(", ")
        return input
    
    def list_order(self, input_list: List[str]) -> List[str]:
        input_list_element_0 = input_list[0]
        input_list.pop(0)
        input_list.sort()
        input_list.insert(0, input_list_element_0)
        return input_list
        
    def lower_case_input (self, input_list: List[str]):
        input_list[0] = input_list[0].lower()
        return input_list
    
    def convert_to_str(self) -> str:
        self.dish_type.pop(0)
        dish_type_str = ", ".join(self.dish_type)
        return dish_type_str
    
