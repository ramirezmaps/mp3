

from random import randint, sample
from secrets import choice

from personas import Cliente, Repartidor, Cocinero
NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]
INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

def crear_repartidores():
    lista_repartidores = []
    for i in range(1,3):
        lista_repartidores.append(Repartidor(choice(NOMBRES)))
    return(lista_repartidores)

def crear_cocineros():
    lista_cocineros = []
    for i in range(1,6):
        lista_cocineros.append(Cocinero(choice(NOMBRES)))
    return(lista_cocineros)

def crear_clientes():
    lista_clientes = []
    for i in range(1,6):
        platos = sample(INFO_PLATOS.keys(),k=randint(1,5))
        lista_platos = []
        for plato in platos:
            lista_platos.append(INFO_PLATOS[plato])
        lista_clientes.append(Cliente(choice(NOMBRES), lista_platos))
    return(lista_clientes)

print(crear_cocineros())



    



        