#En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa.
#Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.
#En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario,
# haréis una operación para calcular el tiempo que queda de trabajo
import time

seconds = time.time()
local_time = time.localtime(seconds)
hora_actual = local_time.tm_hour
def jornada():
    print("Hora actual :", hora_actual, "h")
    if(hora_actual >= 19):
        print("Es hora de ir a casa")
    else:
        a = 19
        b = hora_actual
        restante = a - b
        print("Aún te queda:" ,restante, "h")

jornada()

