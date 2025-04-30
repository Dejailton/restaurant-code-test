

class RestaurantApp:
    def __init__(self):
        self.status = "closed"        

    def open_restaurant(self):
        self.status = "open"
        self.print_status()
    
    def print_status(self):
        print(f"The restaurant is {self.status} !")

    def close_restaurant(self):
        self.status = "closed"
        self.print_status()
