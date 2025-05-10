import pytest
from app.dishes_manager import DishesManager

class TestDishTable:
    @pytest.mark.parametrize("input,expectedOutput", 
    [
        ("", "error"), 
        (",", "error"), 
        ("morning", ""), 
        ("MORNING", ""), 
        ("night", ""), 
        ("NIGHT", ""), 
        ("afternoon", "error"), 
        #("morning, 1, 2, 3", "eggs, toast, coffee"), 
        #("morning, 2, 1, 3", "eggs, toast, coffee"), 
        #("morning, 1, 2, 3, 4", "eggs, toast, coffee, error"), 
        #("morning, 4, 3, 2, 1", "eggs, toast, coffee, error"), 
        #("morning, 3, 2, 1", "eggs, toast, coffee"), 
        #("morning, 2, 1", "eggs, toast"), 
        #("morning, 1", "eggs"), 
        #("morning, 3, 2, 1", "eggs, toast, coffee"), 
        #("morning, 1, 2, 3, 4", "eggs, toast, coffee, error"), 
        #("morning, 1, 2, 3, 3, 3", "eggs, toast, coffee(x3)"),
        #("MORNING  ,  1   ,  2,  3", "eggs, toast, coffee"), 
        #("night, 1, 2, 3, 4", "steak, potato, wine, cake"), 
        #("night, 3, 4, 2, 1", "steak, potato, wine, cake"), 
        #("night, 1, 2, 2, 4", "steak, potato(x2), cake"), 
        #("night, 1, 2, 3, 5", "steak, potato, wine, error"), 
        #("night, 1, 1, 2, 3", "steak, error"),        
        #("night, 4, 3, 2, 1", "steak, potato, wine, cake"), 
        #("night, 3, 2, 1", "steak, potato, wine"), 
        #("night, 2, 1", "steak, potato"), 
        #("night, 1", "steak"),  
    ])
    def test_when_input_then_validate_output(self, input:str, expectedOutput:str):
        # arrange                
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert
        assert currentOutput == expectedOutput
