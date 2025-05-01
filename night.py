from metodos import Metodos

class Night(Metodos):
    def __init__(self) -> None:
        self.entree = "steak"
        self.side = "potato"
        self.drink = "wine"
        self.dessert = "cake"
        
    def imprimir_atributos(self):
        print(self.entree)
        print(self.side)
        print(self.drink)
        print(self.dessert)
        
