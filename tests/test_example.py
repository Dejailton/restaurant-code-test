class ExampleApp:
    def calculate(self):
        return True
    
class TestExampleApp:

    def test_when_conditions_then_results(self):    
        # arrange
        expectedValue = True
        currentValue = False
        app = ExampleApp()
        # act
        currentValue = app.calculate()
        # assert
        assert currentValue == expectedValue