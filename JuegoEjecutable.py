from Tecnicas import Tecnicas
from Personajes import Personajes

tecnica1 = Tecnicas("Cabezazo férreo", 40)
tecnica2 = Tecnicas("Puño de fuego", 70)
tecnica3 = Tecnicas("Patada tornado", 120)


Paco = Personajes("Paco", 50, [tecnica1, tecnica3])
Paco.verPesonaje()




