


class Mascota:
    def __init__(self, name, tipo, golosinas, salud, energia):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = salud
        self.energia = energia


    def dormir(self):
        self.energia += 25
        print("la energía subió")

    def comer(self):
        self.energia += 5
        self.salud += 10

    def jugar(self):
        self.salud += 5 

    def ruido(self):
        print("woof woof")

    