class Formatter:
    def format_lower(self, input: str) -> str:
        return input.lower()
    
    def format_list(self, input: str) -> list:
        input = input.replace(" ", "")
        if input == ",":
            return [","]
        return input.split(",")
    
    def format_output(self, input: list) -> str:
        input = ", ".join(input)
        return input
    
    def list_order(self, input: list) -> list:
        input.pop(0)
        input.sort()
        return input