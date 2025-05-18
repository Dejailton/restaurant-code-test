from typing import List


class DayManager:
    def __init__(self, period, dishes, repetitive_dish):
        self._day = period
        self._dishes = dishes
        self._repetitive_dish = repetitive_dish

    def get_day(self) -> str:
        return self._day
    
    def get_dishes(self) -> List[str]:
        return self._dishes
    
    def get_repetitive_dish(self) -> List[str]:
        return self._repetitive_dish
        
    def get_output_autorized(self, input: List[str]) -> List[str]:
        count = 0
        dishes = []
        dish_repeat = self.get_repetitive_dish()
        
        for i in input:
            if i == dish_repeat[1]:
                count += 1
                if count >= 2:
                    if f"{dish_repeat[0]}(x{count - 1})" in dishes:
                        dishes.remove(f"{dish_repeat[0]}(x{count - 1})")
                    dish = f"{dish_repeat[0]}(x{count})"
                    dishes.append(dish)
            dishes.append(self.get_dishes()[int(i)-1])
            while "coffee" in dishes or "potato" in dishes:
                        dishes.remove(f"{dish_repeat[0]}")
        return dishes

    def dish_uniq(self, dishes: List[str], dishes_on_the_menu, dish):
        uniq = True
        dish = dishes_on_the_menu[int(dish)-1]
        dish_repeat = self.get_repetitive_dish()
        if dish in dishes:
            if dish == dish_repeat[0]:
                return uniq
            else:
                return "error"