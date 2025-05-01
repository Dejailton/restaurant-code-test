from metodos import Metodos

class Morning(Metodos):
    def __init__(self) -> None:
        self.entree = "eggs"
        self.side = "toast"
        self.drink = "coffe"
        self.dessert = "error"
        
    def imprimir_atributos(self):
        print(self.entree)
        print(self.side)
        print(self.drink)
        print(self.dessert)
    