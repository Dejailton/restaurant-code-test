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
        input_list_lower = dishes_table.lower_case_input(input_list_ordered)
        dishes_table.verification_time_of_day(input_list_lower)
        dishes_table_str = dishes_table.convert_to_str()
        output = dishes_table_str
        return output