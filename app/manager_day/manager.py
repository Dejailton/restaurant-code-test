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
        repeat = self.get_repetitive_dish()
        
        for i in input:
            if i == repeat[1]:
                count += 1
                if count >= 2:
                    if f"{repeat[0]}(x{count - 1})" in dishes:
                        dishes.remove(f"{repeat[0]}(x{count - 1})")
                    dish = f"{repeat[0]}(x{count})"
                    dishes.append(dish)
            dishes.append(self.get_dishes()[int(i)-1])
            while "coffee" in dishes or "potato" in dishes:
                        dishes.remove(f"{repeat[0]}")
        return dishes

    def dishe_uniq(self, dishes: List[str], input, period) -> bool:
        uniq = True
        if period == "morning":
            for dish in dishes:
                if dish == "eggs" and input == "1":
                    uniq = False
                    return "error"
                elif dish == "toast" and input == "2":
                    uniq = False
                    return "error"
                elif dish == "error" and input == "4":
                    break
        elif period == "night":
            for dish in dishes:
                if dish == "steak" and input == "1":
                    uniq = False
                    return "error"
                elif dish == "wine" and input == "3":
                    uniq = False
                    return "error"
                elif dish == "cake" and input == "4":
                    uniq = False
                    return "error"
        if uniq:
            return True
        else:
            return False