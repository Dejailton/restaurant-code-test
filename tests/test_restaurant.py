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
        app.close_restaurant()
        currentValue = app.status
        # assert
        assert currentValue == expectedValue
        
    def test_when_input_morning_then_output(self):
        # arrange
        input = "morning"
        expectedOutput = ""
        currentOutput = ""
        app = RestaurantApp()
        # act
        currentOutput = app.process_order(input)
        # assert
        assert currentOutput == expectedOutput
        
    def test_when_input_night_then_output(self):
        # arrange
        input = "night"
        expectedOutput = ""
        currentOutput = ""
        app = RestaurantApp()
        # act
        currentOutput = app.process_order(input)
        # assert
        assert currentOutput == expectedOutput
        
    def test_when_input_night_upper_then_output(self):
        # arrange
        input = "NIGHT"
        expectedOutput = ""
        currentOutput = ""
        app = RestaurantApp()
        # act
        currentOutput = app.process_order(input)
        # assert
        assert currentOutput == expectedOutput
        
    # def test_when_input_morning123_then_output(self):
    #     # arrange
    #     input = "morning, 1, 2, 3"
    #     expectedOutput = "eggs, toast, coffee"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
        
        
    # def test_when_input_morning213_then_output(self):
    #     # arrange
    #     input = "morning, 2, 1, 3"
    #     expectedOutput = "eggs, toast, coffee"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
        
    # def test_when_input_morning1234_then_output(self):
    #     # arrange
    #     input = "morning, 1, 2, 3, 4"
    #     expectedOutput = "eggs, toast, coffee, error"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
        
    # def test_when_input_morning12333_then_output(self):
    #     # arrange
    #     input = "morning, 1, 2, 3, 3, 3"
    #     expectedOutput = "eggs, toast, coffee(x3)"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
        
    # def test_when_input_night1234_then_output(self):
    #     # arrange
    #     input = "night, 1, 2, 3, 4"
    #     expectedOutput = "steak, potato, wine, cake"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
        
    # def test_when_input_night3421_then_output(self):
    #     # arrange
    #     input = "night, 3, 4, 2, 1"
    #     expectedOutput = "steak, potato, wine, cake"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
    
    # def test_when_input_night1224_then_output(self):
    #     # arrange
    #     input = "night, 1, 2, 2, 4"
    #     expectedOutput = "steak, potato(x2), cake"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
    
    # def test_when_input_night1235_then_output(self):
    #     # arrange
    #     input = "night, 1, 2, 3, 5"
    #     expectedOutput = "steak, potato, wine, error"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput
        
    # def test_when_input_night1123_then_output(self):
    #     # arrange
    #     input = "night, 1, 1, 2, 3"
    #     expectedOutput = "steak, error"
    #     currentOutput = ""
    #     app = RestaurantApp()
    #     # act
    #     currentOutput = app.process_order(input)
    #     # assert
    #     assert currentOutput == expectedOutput