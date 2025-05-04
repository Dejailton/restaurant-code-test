from typing import List


class Dishes_Table:
    def __init__(self):
        self.dish_type = ["day", "entree", "side", "drink", "dessert"]
        
    def verification_time_of_day(self) -> None:
        if (self.dish_type[0] == "morning"):
            self.dish_type[1] = "eggs"
            self.dish_type[2] = "toast"
            self.dish_type[3] = "coffee"
            self.dish_type[4] = "Not_Applicable"
            
        elif (self.dish_type[0] == "night"):
            self.dish_type[1] = "steak"
            self.dish_type[2] = "potato"
            self.dish_type[3] = "wine"
            self.dish_type[4] = "cake"
    
    def verification_morning_input_4(self):
        if (self.dish_type[0] == "morning"):
            self.dish_type[4] = "error"
    
    def conversion_to_list(self, input: str) -> List[str]:
        input = input.split(", ")
        return input
    
    def list_order(self, input_list: List[str]) -> List[str]:
        input_list_element_0 = input_list[0]
        input_list.pop(0)
        input_list.sort()
        input_list.insert(0, input_list_element_0)
        return input_list
    
    def print_dishes(self, input_list: List[str]) -> str:
        if (len(input_list) > 4):
            entree = int(input_list[1])
            side = int(input_list[2])
            drink = int(input_list[3])
            self.input_with_repeated_coffee(input_list)
            if (self.dish_type[3] == "coffee(x3)"):
                output = self.dish_type[entree] + ", " + self.dish_type[side] + ", " + self.dish_type[drink]
            else:
                dessert = int(input_list[4])
                output = self.dish_type[entree] + ", " + self.dish_type[side] + ", " + self.dish_type[drink] + ", " + self.dish_type[dessert]
            
        else:
            entree = int(input_list[1])
            side = int(input_list[2])
            drink = int(input_list[3])
            output = self.dish_type[entree] + ", " + self.dish_type[side] + ", " + self.dish_type[drink]
        return output
    
    def input_with_repeated_coffee (self, input_list: List[str]):
        coffee = 0
        for item in input_list:
            if (item == "3"):
                coffee = coffee + 1
        if (coffee >= 2):
            coffee_str = str(coffee)
            self.dish_type[3] = f"coffee(x{coffee_str})"
        elif (coffee == 1):
            self.dish_type[3] = "coffee"