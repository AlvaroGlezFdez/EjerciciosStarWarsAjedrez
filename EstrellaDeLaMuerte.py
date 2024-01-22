


#importar los planetas creados desde la clase de los planetas
from Planetas import Planeta_Concordia,Planeta_Ilum,Planeta_Kamino
#Crear clase de estrella de la muerte
class EstrellaDeLaMuerte:
    def __init__(self):
        self.puntos_de_vida = 1000

    def destruir_planeta(self, planeta):
        if planeta.clasificacion <= self.puntos_de_vida:
            print("La Estrella de la Muerte ha destruido el planeta",planeta.nombre)
            self.puntos_de_vida -= planeta.clasificacion
        else:
            print("La Estrella de la Muerte no puede destruir el planeta",planeta.nombre)

# Crear instancias de planetas y la Estrella de la Muerte
concordia = Planeta_Concordia()
ilum = Planeta_Ilum()
kamino = Planeta_Kamino()
estrella_muerte = EstrellaDeLaMuerte()

# Llamar al método destruir_planeta para cada planeta
estrella_muerte.destruir_planeta(concordia)
estrella_muerte.destruir_planeta(ilum)
estrella_muerte.destruir_planeta(kamino)