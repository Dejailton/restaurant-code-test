from .dishes_table import Dishes_Table

class RestaurantApp:
    def __init__(self):
        self.status = "closed"

    def open_restaurant(self):
        self.status = "open"
        self._print_status()

    def close_restaurant(self):
        self.status = "closed"
        self._print_status()
    
    def _print_status(self)->None:
        print(f"The restaurant is {self.status} !")
        
    def process_order(self, input: str):
        dishes_table = Dishes_Table()
        input_list = dishes_table.conversion_to_list(input)
        print(input_list[0])
        dishes_table.dish_type[0] = input_list[0]
        print(dishes_table.dish_type[0])
        print(input_list[0] == dishes_table.dish_type[0])
        dishes_table.verification_time_of_day()
        entree = int(input_list[1])
        side = int(input_list[2])
        drink = int(input_list[3])
        output = (dishes_table.dish_type[entree] + ", " + dishes_table.dish_type[side] + ", " + dishes_table.dish_type[drink])
        return output