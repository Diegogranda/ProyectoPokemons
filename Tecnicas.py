class Tecnicas:
    nombre = ""
    danyo = 0
    #Constructor
    def __init__(self, nombre, danyo):
        self.nombre = nombre
        self.danyo = danyo


    def verTecnica(self):
        print(self.nombre)
        print(self.danyo)
        print(" ")

