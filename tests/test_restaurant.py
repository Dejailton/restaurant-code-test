from app.restaurant import RestaurantApp

class TestRestaurant: 
    
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