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
        
        if len(input_list) == 0:
            return ''
                
        items = [] 
        
        for input in input_list:
            item = self._get_item(int(input))
            items.append(item)
            if item == "error":
                break            
       
        return ", ".join(items)