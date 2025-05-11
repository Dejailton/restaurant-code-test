class DayManager:
    def __init__(self, period, dishes):
        self._day = period
        self._dishes = dishes

    def get_day(self):
        return self._day
    
    def get_dishes(self):
        return self._dishes
    
    def dishe_sum_autorized(self, input, period, day: object):
        count = 0
        dishes = []
        repeat = ""
        if period == "morning":
            for i in input:
                if i == "3":
                    count += 1
                    if count >= 2:
                        if f"coffee(x{count - 1})" in dishes:
                            dishes.remove(f"coffee(x{count - 1})")
                        repeat = f"coffee(x{count})"
                        dishes.append(repeat)
                dishes.append(day.get_dishes()[int(i)-1])
                while "coffee" in dishes:
                    dishes.remove("coffee")
        elif period == "night":
            for i in input:
                if i == "2":
                    count += 1
                    if count >= 2:
                        if f"potato(x{count - 1})" in dishes:
                            dishes.remove(f"potato(x{count - 1})")
                        repeat = f"potato(x{count})"
                        dishes.append(repeat)
                dishes.append(day.get_dishes()[int(i)-1])
                while "potato" in dishes:
                    dishes.remove("potato")
        return dishes