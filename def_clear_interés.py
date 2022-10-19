from time import sleep
from os import system
from operator import __name__

def clear():
    print("\033[1;32;40m")
    if __name__ == 'nl':
        system("cls")
    else:
        system("clear")
    sleep(2)
clear()

print("\nCalculo de los intereses producidos\n")
sleep(1)
c=float(input("Dime cuanto has invertido\n"))
sleep(1)
r=float(input("\nDime el interes aplicado\n"))
sleep(1)
t=float(input("\n¿En cuantos dias?\n"))
sleep(2)
print("\nAplicamos la formula Y = c x r x t / 360 x 100\n")
sleep(2)
print("\nResultado Y =",(c*r*t)//(360*100)+c,"\n")
sleep(2)
print("\nFinal\n")
sleep(2)