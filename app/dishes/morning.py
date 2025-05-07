from .common import CommonDishes

class MorningDishes(CommonDishes):
    def __init__(self):
        period = "morning"        
        menu = ['eggs', 'toast', 'coffee']
        super().__init__(period=period, menu=menu)