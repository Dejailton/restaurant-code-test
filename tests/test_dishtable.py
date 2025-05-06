from app.dishes_table import DishTable


class TestDishTable:     
        
    def test_when_input_morning_then_output(self):
        # arrange
        input = "1,2,3"
        period = "morning"
        expectedPeriod = "morning"
        expectedItems = "eggs, toast, coffee"
        
        dish = DishTable(period=period)
        # act
        currentOutput = dish.get_items(input)
        # assert
        assert expectedPeriod == dish.get_period()
        assert currentOutput == expectedItems
        
    def test_when_input_morning_upper_then_output(self):
        # arrange
        input = "1,2,3"
        period = "MORNING"
        expectedPeriod = "morning"
        expectedItems = "eggs, toast, coffee"
        
        dish = DishTable(period=period)
        # act
        currentOutput = dish.get_items(input)
        # assert
        assert expectedPeriod == dish.get_period()
        assert currentOutput == expectedItems
        
    def test_when_input_morning_upper_space_then_output(self):
        # arrange
        input = "1   ,  2, 3"
        period = "MORNING"
        expectedPeriod = "morning"
        expectedItems = "eggs, toast, coffee"
        
        dish = DishTable(period=period)
        # act
        currentOutput = dish.get_items(input)
        # assert
        assert expectedPeriod == dish.get_period()
        assert currentOutput == expectedItems