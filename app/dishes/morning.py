from app.dishes.common import CommonDishes

class MorningDishes(CommonDishes):
    def __init__(self):
        period = "morning"        
        menu_options = ['eggs', 'toast', 'coffee']
        repeatable_options = ['coffee']
        super().__init__(period=period, menu_options=menu_options, repeatable_options=repeatable_options)   
    