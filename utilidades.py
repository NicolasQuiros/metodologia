from random import randint
from random import seed

#Generar un numero aleatorio entre un maximo y minimo.
def generador_numero_aleatorio(min, maximo):
    seed()
    return randint(min, maximo)
def reaccion_tux():
    print("Hola joven princesa, que sistema operativo te parece el mejor?")
    so_eleccion = input("Linux(0)/MacOS(1)/Windows(2)")
    if so_eleccion == "2":
        print("Me das lastima jovencita.")