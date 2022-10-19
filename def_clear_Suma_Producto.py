from time import sleep
from os import system
from operator import __name__

def clear():
    if __name__ == 'nl':
        system("cls")
    else:
        system("clear")
    sleep(2)

def changeBackground():
    print("\033[1;32;40m")
    clear()

changeBackground()

print("\nIniciando el programa...")

sleep(1)

nom=input("\nDime tu nombre:\n")

print("\nHola",nom,"\nNecesito tres valores\n")

sleep(2)

num=int(input("Dime primero un numero entero\n"))

real1=float(input("\nDime un numero real\n"))
real2=float(input("\nY ahora otro, tambien real\n"))

print("\nResultados\n")
sleep(1)
print("Sumando:",num,"+",real1,"+",real2,"= {:>6.2f}".format(num+real1+real2),"\n")
sleep(2)
print("Producto",num,"*",real1,"*",real2,"= {:>6.2f}".format(num*real1*real2),"\n")
sleep(2)
print("Division del resultado del producto entre suma {:>6.2f}".format((num*real1*real2)/(num+real1+real2)),"\n")
sleep(2)
print("Division entera del producto y la suma",(num*real1*real2)//(num+real1+real2),"\n")
sleep(2)
print("El resto de la division entera {:>6.2f}".format((num*real1*real2)%(num+real1+real2)),"\n")
sleep(4)