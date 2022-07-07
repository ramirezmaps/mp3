from random import choices, randrange
from secrets import choice


PLATOS_PRUEBA ={
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}


# Usamos asignación múltiple, para seleccionar la clave y valor del elemento del diccionario, aleatoriamente seleccionado.
# Nótese como realizamos una conversión a lista de los elementos del diccionario para hacer uso del método choice.
clave, valor = choices(list(PLATOS_PRUEBA.items()))
print(clave, valor)

