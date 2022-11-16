class Vehiculo():
     color = "rojo"
     ruedas = 4
     puertas = 5

class Coche(Vehiculo):
     velocidad = 120
     cilindrada = 1500

c = Coche()
print("La velocidad del coche es " +  str(c.velocidad))
