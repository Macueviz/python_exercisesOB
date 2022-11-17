
def escribe(fichero, datos):
    f = open(fichero, 'w')

    for linea in datos:
        if not linea.endswith('\n'):
            linea += '\n'
        f.write(linea)

    f.close()

lista = [
    'Hola',
    '¿Qué tal?',
    'Soy un fichero'
]
escribe('mifichero.txt', lista)

leer = open('mifichero.txt', 'r')
datos = leer.read()
leer.close()

print(datos)