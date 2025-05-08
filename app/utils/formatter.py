from typing import List


class Formatter:
    def __init__(self):
        self._period = ""
    
    def get_period(self) -> str:
        return self._period
    
    def conversion_to_list(self, input: str) -> List[str]:
        input = input.replace(" ", "")
        input_list = input.split(",")
        return input_list
    
    def lower_case_input (self, input_list: List[str]):
        input_list[0] = input_list[0].lower()
        return input_list
    
    def list_order(self, input_list: List[str]):
        self._period = input_list[0]
        if len(input_list) > 1:
            input_list.pop(0)
            input_list.sort()
        return input_list
    
    def get_length(self, input_list: List[str]) -> int:
        return len(input_list)
        
    def equal_index(self, input_list: List[str]):
        for i in range(len(input_list)):
            input_list[i] = int(input_list[i]) - 1
        return input_list
    
    def convert_to_str(self, input: List[str]) -> str:
        return ', '.join(input)
        input_str = ", ".join(input)
        return input_str
    
    def formatting(self, input: str):
        input_list = self.conversion_to_list(input)
        input_list = self.lower_case_input(input_list)
        input_list = self.list_order(input_list)
        return input_list
    
    def formatter_index(self, input_list: List[str]) -> List[str]:
        nova_lista = []
        for i in input_list:
            numero = int(i)
            numero -= 1
            nova_lista.append(numero)
        return nova_lista