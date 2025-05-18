from typing import List


class DayManager:
    def __init__(self, period, dishes, repetitive_dish):
        self._period = period
        self._dishes = dishes
        self._repetitive_dish = repetitive_dish

    def get_period(self) -> str:
        return self._period
    
    def get_dishes(self) -> List[str]:
        return self._dishes
    
    def get_repetitive_dish(self) -> List[str]:
        return self._repetitive_dish
        
    def get_output_autorized(self, inputs: List[str], repetitive_dish) -> List[str]:
        count = 0
        dishes = []
        dish_repeat = repetitive_dish
        for i in inputs:
            if i == dish_repeat[1]:
                count += 1
                if count >= 2:
                    if f"{dish_repeat[0]}(x{count - 1})" in dishes:
                        dishes.remove(f"{dish_repeat[0]}(x{count - 1})")
                    dish = f"{dish_repeat[0]}(x{count})"
                    dishes.append(dish)
            else:
                dishes.append(self.get_dishes()[int(i)-1])

        return dishes
    
    def dish_verify(self, dishes: List[str], dishes_on_the_menu, dish) -> bool:
        dish_int = int(dish)
        dish_repeat = self.get_repetitive_dish()
        if dish_int >= 5 or dish_int <= 0:
            return True
        else:
            dish = dishes_on_the_menu[int(dish)-1]
            if dish in dishes:
                if dish == dish_repeat[0]:
                    return False
                else:
                    return True
        