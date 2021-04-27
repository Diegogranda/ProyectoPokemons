from Tecnicas import Tecnicas

class Personajes:
    nombre = ""
    vida = 0
    tecnicas = []

    #Constructor
    def __init__(self, nombre, vida, tecnicas):
        self.nombre = nombre
        self.vida = vida
        self.tecnicas = tecnicas

    def getNombre(self):
        print(self.nombre)

    def getVida(self):
        print(self.vida)

    def getTecnicas(self):
        for x in self.tecnicas:
            Tecnicas.verTecnica(x)

    def verPesonaje(self):
        print(self.nombre)
        print(self.vida)
        self.getTecnicas()

