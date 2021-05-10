import  random
from Tecnicas import Tecnicas
from Personajes import Personajes


def turno(jugador, IA, movimiento):
    habilidad = jugador.tecnicas[movimiento-1]
    print(jugador.getNombre(), "Has elegido la habilidad", habilidad.nombre)
    IA.setvida(habilidad.getdanyo())
    IA.vervidaactual()


def turnoIA(IA, jugador):
    indice = random.randint(1,len(IA.tecnicas))
    movimiento= IA.tecnicas[indice-1]
    print(IA.getNombre(), ", la inteligencia artificial contrincante ha elegido la habilidad :", movimiento.nombre)
    jugador.setvida(movimiento.getdanyo())
    jugador.vervidaactual()


def confirmacionpersonaje():
    confirmacionpersonaje = str(input("¿Esta de acuerdo en elegir este personaje presione s/n "))

    if confirmacionpersonaje == "s":
        print("Personaje elegido correctamente")
    elif confirmacionpersonaje == "n":
        print("Personaje no elegido, elija otro distinto")
        input()
        menu()
    else:
        print("Ninguna de las opciones es correcta")


tecnica1 = Tecnicas("Cabezazo férreo", 40)
tecnica2 = Tecnicas("Puño de fuego", 70)
tecnica3 = Tecnicas("Patada tornado", 120)
tecnica4 = Tecnicas("Mano Celestial", 124)
tecnica5 = Tecnicas("Colmillo Veneno", 105)


Personaje1 = Personajes("Veigar", 770, [tecnica2, tecnica3])
Personaje2 = Personajes("Marth", 500, [tecnica1, tecnica5])
Personaje3 = Personajes("Luiska", 450, [tecnica1, tecnica3])
Personaje4 = Personajes("Totoro", 950, [tecnica5, tecnica3])
Personaje5 = Personajes("Abarosa", 1050, [tecnica1, tecnica4])

Personajes = [Personaje1,Personaje2, Personaje3, Personaje4, Personaje5]







def menu():
    """

    Función que limpia la pantalla y muestra nuevamente el menu

    """

   # os.system('cls')

    print(" Selecciona tu personaje para el combate")

    print("\t1 - Veigar")

    print("\t2 - Marth")

    print("\t3 - Luiska")

    print("\t4 - Totoro")

    print("\t5 - Abarosa")


    print("\t9 - salir")

y=0
while y== 0:

    # Mostramos el menu

    menu()

    # solicituamos una opción al usuario

    opcionMenu = input("Elige un numero de personaje: ")

    if opcionMenu == "1" or opcionMenu == "2" or opcionMenu == "3" or opcionMenu == "4" or opcionMenu == "5":

        print(" ")
        x = (int(opcionMenu)) - 1
        input("Has elegido a "+Personajes[x].getNombre()+"!!!\n-Pulsa una tecla para ver sus características")
        print("")
        print("Sus características son:")

        Personajes[x].vercaracteristicas()
        input()
        confirmacionpersonaje()
        input()
        jugador1 = Personajes[x]
        Personajes.pop(x, )
        enemi= random.choice(Personajes)
        print("La inteligencia artificial está eligiendo un personaje...")
        input()
        print("El personaje elegido por la Inteligencia Artificial es: ", enemi.getNombre())


        while jugador1.getvidaint()>0 and enemi.getvidaint()>0:
            input()
            print("")
            print("¿QUE HABILIDAD DESEA REALIZAR LA 1 o 2?")
            print("")
            jugador1.getTecnicas()
            habilidad = int(input())
            turno(jugador1,enemi,habilidad)
            if enemi.getvidaint() <= 0:
                print("Has ganado el combate")
                y = 1
            turnoIA(enemi,jugador1)
            if jugador1.getvidaint() <= 0:
                print("El enemigo ha ganado el combate")
                y = 1








    elif opcionMenu == "9":

        y=1

    else:

        print("")

        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")



















