

class Ninja:
    def __init__(self,nombre, apellido,mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio 
        self.comida_mascota = comida_mascota


    def caminar(self):
        self.mascota.jugar()

    def alimentar(self):
        self.mascota.comer()

    def bañar(self):
        self.mascota.ruido()