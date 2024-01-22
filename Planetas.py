

#ARCHIVO QUE RECOGE LA CLASE PLANETAS CON SUS RESPECTIVAS CLASES HIJAS


#Creación de una clase para los planetas y sus características
class Planeta:
    def __init__(self, nombre, volumen, clasificacion):
        self.nombre = nombre
        self.volumen = volumen
        self.clasificacion = clasificacion

#Creación del planeta concordiaa (super init para herencia de la clase Planetas )
class PlanetaConcordia(Planeta):
    def __init__(self):
        super().__init__("Concordia", 500, 1)

#Creación del planeta Ilum (super init para herencia de la clase Planetas )
class Planeta_Ilum(Planeta):
    def __init__(self):
        super().__init__("Ilum", 1200, 2)

#Creación del planeta Kamino (super init para herencia de la clase Planetas )
class Planeta_Kamino(Planeta):
    def __init__(self):
        super().__init__("Kamino", 800, 3)
