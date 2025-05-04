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
        input_list_ordered = dishes_table.list_order(input_list)
        dishes_table.dish_type[0] = input_list[0]
        dishes_table.verification_time_of_day()
        dishes_table.verification_morning_input_4()
        output = dishes_table.print_dishes(input_list_ordered)
        return output
    