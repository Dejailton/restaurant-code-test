from .common import CommonDishes

class NightDishes(CommonDishes):
    def __init__(self):
        period = "night"        
        menu_options = ['steak', 'potato', 'wine', 'cake']
        repeatable_options = ['potato']
        super().__init__(period=period, menu_options=menu_options, repeatable_options=repeatable_options)
