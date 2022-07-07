
from personas import Cliente, Cocinero, Repartidor
##############################################################
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self, nombre, platos = {}, cocineros = [], repartidores = []):
        self.nombre = nombre
        self.platos = platos
        self.cocineros = cocineros
        self.repartidores = repartidores
        self.calificacion = 0
        
        
    
    def recibir_pedidos(self, clientes):
        for cliente in clientes:
            pedido = []
            print(f"El Nombre del cliente es: {cliente.nombre}")
            for plato in cliente.platos_preferidos:
                informacion_plato = self.platos[plato]
                self.cocineros.sort(reverse=True, key=lambda x: x.habilidad)
                for cocinero in self.cocineros:
                    if cocinero.energia > 0:
                        r = cocinero.cocinar(informacion_plato)
                        pedido.append(r)
                        break
            self.repartidores.sort(reverse=False, key=lambda x: x.tiempo_entrega)
            for repartidor in self.repartidores:
                if repartidor.energia > 0:
                    tiempo_de_entrega = repartidor.repartir(pedido)
                    self.calificacion += cliente.recibir_pedido(pedido, tiempo_de_entrega)
                    break
                else:
                    self.calificacion += cliente.recibir_pedido([],0)
        self.calificacion = self.calificacion / len(clientes)
        print(str(self.calificacion))
                    
### FIN PARTE 3 #

if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
