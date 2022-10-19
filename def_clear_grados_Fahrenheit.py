from time import sleep
from os import system
from operator import __name__

def clear():
    if __name__ == 'nl':
        system("cls")
    else:
        system("clear")
    sleep(1)

def change_Background():
    print("\033[1;32;40m")
    clear()

change_Background()

print("\nPasar de grados Fahrenheit a Centígrados ...\n")
sleep(1)
f=float(input("Introduce los grados Fahrenheit\n"))
sleep(1)
print("\nAplicamos la formula C=5/9(F-32)")
sleep(1)
print("\nResultado: C =",5/9*(f-32))
sleep(4)
print("\nFinal\n")
sleep(2)