from itertools import count
from random import shuffle
from xml.dom.expatbuilder import theDOMImplementation


lista = []
cadena = str ( input ("\nIntroduce una cadena: "))

espacios = list(cadena.split(" "))

for i in espacios:
    if (i not in lista):
        lista.append(i)
        lista.append(espacios.count(i))
diccionario = {lista[a]:lista[a + 1] for a in range(0, len(lista), 2)}
print(diccionario)