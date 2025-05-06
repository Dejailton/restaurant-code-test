class CommonDishes:
    def __init__(self, period:str, menu:list):
        self._period = period 
        self._menu = menu                      
        
    def get_period(self) -> str:
        return self._period
    
    def _get_item(self, index:int) -> str:    
        index -=1    
        if index < 0 or index >= len(self._menu):
            return "error"
        
        return self._menu[index]

    def get_order_items(self, input_list: list[str]) -> str:        
        items = [] 
        
        for input in input_list:       
            items.append(self._get_item(int(input)))
       
        return ", ".join(items)