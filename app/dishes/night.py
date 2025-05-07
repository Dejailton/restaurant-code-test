from .common import CommonDishes

class NightDishes(CommonDishes):
    def __init__(self):
        period = "night"        
        menu = ['steak', 'potato', 'wine', 'cake']
        super().__init__(period=period, menu=menu)