from .class_day.morning import Morning

class DishesManager(Morning):
    def __init__(self):
        self.dishes = {}
    
    def verify_input(self, input:str) -> str:
        if input == "morning":
            return super().get_period()
        else:
            return "error"
    def process_order(self, input: str):
        output = self.verify_input(input)
        return output
        
        
   
        
        

        
        
        
    
