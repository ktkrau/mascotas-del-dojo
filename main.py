from Ninja import Ninja
from Mascota import Mascota


mascota1 = Mascota("Bruna","perro", "galletas", 10, 10)
ninja1 = Ninja("Katherine", "Kraushaar",mascota1, 2, "pelet")



ninja1.caminar()

ninja1.alimentar()
ninja1.bañar()

print(mascota1.energia)
print(mascota1.salud)