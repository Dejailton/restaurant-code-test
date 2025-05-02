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
        
    def test_when_input_morning123_then_output(self):
        # arrange
        input = "morning, 1, 2, 3"
        expectedOutput = "eggs, toast, coffee"
        currentOutput = ""
        app = RestaurantApp()
        # act
        currentOutput = app.process_order(input)
        # assert
        assert currentOutput == expectedOutput