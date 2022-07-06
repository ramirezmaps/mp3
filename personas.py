##############################################################
from random import choices, randint, choice
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nombre, tiempo_entrega = randint(20,30)):
        super().__init__(nombre)
        self.tiempo_entrega = tiempo_entrega
        self.energia = randint(75,100)

    # def repartir(self, pedido):
    #     if len(pedido) <=2:
    #         self.energia = self.energia - 5
    #         factor_velocidad = self.tiempo_entrega * 1.25
    #         return (factor_velocidad)
    #     else:
    #         self.energia = self.energia - 15
    #         factor_velocidad = self.tiempo_entrega * 0.85
    #         return(factor_velocidad)


### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nombre, habilidad = randint(1,10)):
        super().__init__(nombre)
        self.habilidad = habilidad
        self.energia = randint(50,80)

    # def cocinar(self, informacion_plato):
    #     pass

### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nombre, platos_preferidos = {}):
        super().__init__(nombre)
        self.platos_preferidos = platos_preferidos #definir elegir n elementos desde el diccionario

    def recibir_pedido(self, pedido, demora):
        calificacion = 10
        if len(pedido) < len(self.platos_preferidos) or demora >=20:
            calificacion = calificacion /2
        for plato in pedido:
            if plato.calidad >= 11:
                calificacion = calificacion + 1.5
            elif plato.calidad <=8:
                calificacion = calificacion - 3
            else:
                pass
        return(calificacion)

### FIN PARTE 2.4 ###

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
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
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        # un_cocinero = Cocinero("Juan")
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)

        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
