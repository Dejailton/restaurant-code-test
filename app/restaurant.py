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