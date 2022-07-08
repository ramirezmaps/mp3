##############################################################
from random import seed
from random import randint, sample
from secrets import choice
from personas import Cliente, Cocinero, Repartidor
from restaurante import Restaurante

## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 4 ###

def crear_cocineros():
    lista_cocineros = []
    for i in range(1,6):
        lista_cocineros.append(Cocinero(choice(NOMBRES)))
    return(lista_cocineros)


def crear_repartidores():
    lista_repartidores = []
    for i in range(1,3):
        lista_repartidores.append(Repartidor(choice(NOMBRES)))
    return(lista_repartidores)
    

def crear_clientes():
    lista_clientes = []
    for i in range(1,6):
        platos = sample(INFO_PLATOS.keys(),k=randint(1,5))
        lista_platos = []
        for plato in platos:
            lista_platos.append(INFO_PLATOS[plato])
        lista_clientes.append(Cliente(choice(NOMBRES), lista_platos))
    return(lista_clientes)
        


def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    restaurante = Restaurante("El_Cocina_Datos", INFO_PLATOS,cocineros,repartidores)
    return(restaurante)
    
    

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################
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

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed("With Love")
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
