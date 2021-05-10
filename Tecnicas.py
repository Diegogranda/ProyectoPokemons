class Tecnicas:
    nombre = ""
    danyo = 0
    #Constructor
    def __init__(self, nombre, danyo):
        self.nombre = nombre
        self.danyo = danyo


    def verTecnica(self):
        print("Habilidad: ",self.nombre)
        print("Realiza",str(self.danyo) + " puntos de daño")
        print("")

    def getdanyo(self):
        return self.danyo



