class Morning:
    def __init__(self):
        self._period = "morning"
        self._dishes = ["eggs", "toast", "coffee"]
        
    def get_period(self):
        return self._period
    
    def get_dishes(self):
        return self._dishes