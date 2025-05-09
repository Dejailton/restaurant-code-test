from .class_day.morning import Morning

class DishesManager(Morning):
    def __init__(self):
        self.dishes = {}
    
    def manager_output(self, input:str) -> str:
        match input:
                case "":
                    return "error"
                case "morning":
                    return ""
    def process_order(self, input: str):
        output = self.manager_output(input)
        return output
        
        
   
        
        

        
        
        
    
