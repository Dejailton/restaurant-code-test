#import pytest #comentado, utilizando test_dishes como base de testes
from app.restaurant import RestaurantApp

class TestRestaurantApp:
    def test_when_create_app_then_status_closed(self):
        # arrange
        expectedValue = "closed"
        currentValue = ""
        app = RestaurantApp()
        # act
        currentValue = app.status
        # assert
        assert currentValue == expectedValue

    def test_when_open_restaurant_then_status_open(self):
        # arrange
        expectedValue = "open"
        currentValue = ""
        app = RestaurantApp()
        # act
        app.open_restaurant()
        currentValue = app.status
        # assert
        assert currentValue == expectedValue
        
    def test_when_close_restaurant_then_status_closed(self):
        # arrange
        expectedValue = "closed"
        currentValue = ""
        app = RestaurantApp()
        # act
        app.open_restaurant()
        currentValue = app.status
        # assert
        assert currentValue == expectedValue
      
    # @pytest.mark.parametrize("input,expectedOutput", 
    # [
    #     ("", "error"), 
    #     (",", "error"), 
    #     ("morning", ""), 
    #     ("MORNING", ""), 
    #     ("night", ""), 
    #     ("NIGHT", ""), 
    #     ("afternoon", "error"), 
    #     ("morning, 1, 2, 3", "eggs, toast, coffee"), 
    #     ("morning, 2, 1, 3", "eggs, toast, coffee"), 
    #     ("morning, 1, 2, 3, 4", "eggs, toast, coffee, error"), 
    #     ("morning, 4, 3, 2, 1", "eggs, toast, coffee, error"), 
    #     ("morning, 3, 2, 1", "eggs, toast, coffee"), 
    #     ("morning, 2, 1", "eggs, toast"), 
    #     ("morning, 1", "eggs"), 
    #     ("morning, 3, 2, 1", "eggs, toast, coffee"), 
    #     ("morning, 1, 2, 3, 4", "eggs, toast, coffee, error"), 
    #     ("morning, 1, 2, 3, 3, 3", "eggs, toast, coffee(x3)"),
    #     ("MORNING  ,  1   ,  2,  3", "eggs, toast, coffee"), 
    #     ("night, 1, 2, 3, 4", "steak, potato, wine, cake"), 
    #     ("night, 3, 4, 2, 1", "steak, potato, wine, cake"), 
    #     ("night, 1, 2, 2, 4", "steak, potato(x2), cake"), 
    #     ("night, 1, 2, 3, 5", "steak, potato, wine, error"), 
    #     ("night, 1, 1, 2, 3", "steak, error"),        
    #     ("night, 4, 3, 2, 1", "steak, potato, wine, cake"), 
    #     ("night, 3, 2, 1", "steak, potato, wine"), 
    #     ("night, 2, 1", "steak, potato"), 
    #     ("night, 1", "steak"),
    # ])
    # def test_when_input_then_validate_output(self, input:str, expectedOutput:str):
    #     # arrange
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
