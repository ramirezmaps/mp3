import random
# DICCIONARIO:
paises = {'PERÚ':'LIMA', 'ESPAÑA':'MADRID', 'BOLIVIA':'SUCRE', 'MÉXICO':'CIUDAD DE MÉXICO', 'ARGENTINA':'BUENOS AIRES', 'PORTUGAL':'LISBOA', 'FILIPINAS':'MANILA'}

# Usamos asignación múltiple, para seleccionar la clave y valor del elemento del diccionario, aleatoriamente seleccionado.
# Nótese como realizamos una conversión a lista de los elementos del diccionario para hacer uso del método choice.
pais, capital = random.choice(list(paises.items()))
print("\nPaís elegido:", pais, "=>", capital)
