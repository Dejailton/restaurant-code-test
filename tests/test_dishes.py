from app.dishes_manager import DishesManager

class TestDishTable:     
    
    def test_when_input_empty_then_output(self):
        # arrange
        input = ""        
        expectedItems = "error"        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
        
    def test_when_input_comma_then_output(self):
        # arrange
        input = ","        
        expectedItems = "error"        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
        
    def test_when_input_morning_noitems_then_output(self):
        # arrange
        input = "morning"        
        expectedItems = ""        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
        
    def test_when_input_night_noitems_then_output(self):
        # arrange
        input = "night"        
        expectedItems = ""        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
    
    def test_when_input_afternoon_noitems_then_output(self):
        # arrange
        input = "afternoon"        
        expectedItems = "error"        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
        
    def test_when_input_morning_then_output(self):
        # arrange
        input = "morning,1,2,3"        
        expectedItems = "eggs, toast, coffee"        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
        
    def test_when_input_morning_upper_then_output(self):
        # arrange
        input = "MORNING, 1,2,3"
        expectedItems = "eggs, toast, coffee"        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems
        
    def test_when_input_morning_upper_space_then_output(self):
        # arrange
        input = "MORNING  ,  1   ,  2,  3"                
        expectedItems = "eggs, toast, coffee"        
        manager = DishesManager()
        # act
        currentOutput = manager.process_order(input)
        # assert        
        assert currentOutput == expectedItems