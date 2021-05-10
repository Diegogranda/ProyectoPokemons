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
        return (self.nombre)

    def getVida(self):
        return (str(self.vida) +" puntos de vida" )

    def getvidaint(self):
        return (self.vida)

    def setvida (self, danyo):
        self.vida= self.vida-danyo

    def getTecnicas(self):
        for x in self.tecnicas:
            x.verTecnica()

    def verPesonaje(self):
        print(self.nombre)
        print(self.vida)
        self.getTecnicas()
        print(" ")

    def vercaracteristicas(self):
        print(self.getVida())
        self.getTecnicas()
        print(" ")

    def vervidaactual (self):
       print( "Puntos de vida restantes: ",self.getVida())










