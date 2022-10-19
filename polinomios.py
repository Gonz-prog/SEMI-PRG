from time import sleep
from math import sqrt
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

print("\nPolinomios de grado 5...\n")
sleep(2)
a, b, c, d=int(input("Dime el valor de la a\n")),int(input("\nDime el valor de la b\n")),int(input("\nDime el valor de c\n")),int(input("\nDime el valor de la d\n"))
sleep(2)
print("\n\t\t",a,"x⁵ -",b,"x³ +",c,"x -",d)
sleep(2)
x=-10
polinomio=a*x**5-b*x**3+c*x-d
print("\nSi x = -10\n",a," · ",x,"⁵ -",b," · ",x,"³ +",c," · ",x," -",d," = ",polinomio)
sleep(2)
x=-1
polinomio=a*x**5-b*x**3+c*x-d
print("\nSi x = -1\n",a," · ",x,"⁵ -",b," · ",x,"³ +",c," · ",x," -",d," = ",polinomio)
sleep(2)
x=0
polinomio=a*x**5-b*x**3+c*x-d
print("\nSi x = 0\n",a," · ",x,"⁵ -",b," · ",x,"³ +",c," · ",x," -",d," = ",polinomio)
sleep(2)
x=1
polinomio=a*x**5-b*x**3+c*x-d
print("\nSi x = 1\n",a," · ",x,"⁵ -",b," · ",x,"³ +",c," · ",x," -",d," = ",polinomio)
sleep(2)
x=10
polinomio=a*x**5-b*x**3+c*x-d
print("\nSi x = 10\n",a," · ",x,"⁵ -",b," · ",x,"³ +",c," · ",x," -",d," = ",polinomio)
sleep(2)
print("\nFinal\n")