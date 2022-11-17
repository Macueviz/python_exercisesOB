import pickle
class Vehiculo:
    marca = ''
    color = ''
    velocidad = 0

    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def getMarca(self):
        return self.marca

# v = Vehiculo('Mercedes', 'Gris', 150)
# f = open('datos.bin', 'wb')
# pickle.dump(v, f)
# f.close()
f = open('datos.bin', 'rb')
coche = pickle.load(f)
f.close()
print('La marca es:',coche.getMarca(),'y el color es:', coche.color)

