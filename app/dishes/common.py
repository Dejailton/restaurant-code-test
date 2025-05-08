class CommonDishes:
    def __init__(self, period:str, menu_options:list[str], repeatable_options:list[str]) -> None:
        self._period = period
        self._repeatable_options = repeatable_options
        self._menu_options = menu_options                      
        
    def get_period(self) -> str:
        return self._period
    
    def _get_item_name(self, index:int) -> str:
        index -=1    
        if index < 0 or index >= len(self._menu_options):
            return "error"        
        return self._menu_options[index]

    def process_order(self, input_list: list[str]) -> str:        
        input_list.sort()
        input_dict = self._get_input_repeat_count(input_list=input_list)
        option_list = self._get_option_list(input_dict=input_dict)       
        return ", ".join(option_list)
    
    def _get_input_repeat_count(self, input_list:list[str]) -> dict[str, int]:
        input_dict: dict[str, int] = {}       
        for i in range(len(input_list)):
            input = input_list[i]            
            if input in input_dict:
                input_dict[input] += 1
            else:
               input_dict[input] = 1
        return input_dict
    
    def _get_option_list(self, input_dict:dict[str, int]) -> list[str]:
        option_list:list[str] = []
        for input in input_dict:            
            repeat_count = input_dict[input]
            option = self._get_item_name(int(input)) 
            
            if repeat_count > 1:            
                if option in self._repeatable_options:
                    option = f"{option}(x{repeat_count})"
                else:
                    option_list.append(option)
                    option = "error"
                      
            option_list.append(option)
            
            if option == "error": 
                break
            
        return option_list