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
        validation = self.verification_quantity_request_drinks_morning(input_list)
        if self.dish_type[0] == "morning":
            for i in input_list:
                match i:
                    case "1":
                        self.dish_type.append(self.morning.get_entree())
                    case "2":
                        self.dish_type.append(self.morning.get_side())
                    case "3":
                        if validation < 1:
                            self.dish_type.append(self.morning.get_drink())
                    case "4":
                        self.dish_type.append(self.morning.get_dessert())
            if validation != False:
                self.dish_type.append(f"coffee(x{validation})")
                        
    def return_dishes_night(self, input_list):
        validation = self.verification_quantity_request_side_night(input_list)
        count = 0
        if self.dish_type[0] == "night":
            for i in input_list:
                match i:
                    case "1":
                        if count == 0:
                            count += 1
                            self.dish_type.append(self.night.get_entree())
                        elif count == 1:
                            self.dish_type.append(self.night.get_error())
                            break
                    case "2":
                        if validation > 1 and validation < 49:
                            if (self.dish_type.append(f"potato(x{validation})") == None):
                                validation = 51
                        elif validation < 1:
                            self.dish_type.append(self.night.get_side())
                    case "3":
                        self.dish_type.append(self.night.get_drink())
                    case "4":
                        self.dish_type.append(self.night.get_dessert())
                    case "5":
                        self.dish_type.append(self.night.get_error())
            
                        
    def verification_quantity_request_drinks_morning(self, input_list):
        drink = 0
        for i in input_list:
            if (i == "3"):
                drink += 1
        if drink > 1:
            return drink
        else:
            return False
        
    def verification_quantity_request_side_night(self, input_list):
        side = 0
        for i in input_list:
            if (i == "2"):
                side += 1
        if side > 1:
            return side
        else:
            return False
                    
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
    
