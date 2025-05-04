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
    
    def conversion_to_list(self, input: str):
        input = input.split(", ")
        return input
    
    def verification_lenght(self, input_list):
        lenght = len(input_list)
        return lenght
    
    