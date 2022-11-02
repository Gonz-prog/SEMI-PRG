from time import sleep
from os import system
from operator import __name__
import math

def clear():
    
    if __name__ == 'nl':
        system("cls")
    else:
        system("clear")
    sleep(1)

def my_printing(d, m, a):
    
    print("\nFecha valida")
    print("(",flush=True,end="")
    print(d,flush=True,end=", ")
    print(m,flush=True,end=", ")
    print(a,flush=True,end=")\n")

def format_fecha(d, m, a, calendario):
    
    print("\nFormato largo")
    print("**",flush=True,end="")
    print(d,flush=True,end=" ")
    print("de",calendario[m - 1][0],"de",flush=True,end=" ")
    print(a,flush=True,end="**\n")

def change_Background():
    
    print("\033[1;32;40m")
    
    clear()

def sumatorioN(n):
    
    change_Background()
    
    n = int ( input ("\n\t\t\t\t   Sumatorio (n): "))
    
    cont = 0
    print("")
    print("Su sumatorio: ",flush=True,end="")
    for i in range(1, n + 1):
        cont += i
        if (i == n):
            print(i,flush=True,end=" = ")
        else:
            print(i,flush=True,end=" + ")
    print(cont)
    print("")

def productorioN(n):
    
    change_Background()
    
    n = int ( input ("\n\t\t\t\t   Productorio (n): "))
    
    cont = 1
    
    print("")
    
    print("Su productorio: ",flush=True,end="")
    
    for i in range(1, n + 1):
        cont *= i
        if (i == n):
            print(i,flush=True,end=" = ")
        else:
            print(i,flush=True,end=" · ")
    
    print(cont)
    print("")

def intermedioN(n):
    
    change_Background()
    
    n = int ( input ("\n\t\t\t\t   Intermedio (n): "))
    
    lista = []
    
    cont = 0
    for i in range(1, n + 1):
        cont += i
        lista.append(i)
    avg = cont / len(lista)
    
    if (avg%1 == 0):
        print("\nEl valor intermedio entre 1 y",n,":",avg,"\n")
    else:
        mid_pos = math.floor(len(lista) / 2)
        avg1 = lista[mid_pos]
        avg2 = lista[mid_pos + 1]
        new_avg = (avg1 + avg2) / 2
        print("\nEl valor intermedio entre 1 y",n,":",new_avg,"(",avg1," + ",avg2,"/ 2)\n")

def esTriangulo(a, b, c):
    
    change_Background()
    
    print("\n\t\t\t¿Se puede hacer un triangulo con los lados a, b y c?\n")
    
    a, b, c = int ( input ("\n\t\ta: ")), int ( input ("\t\tb: ")), int ( input ("\t\tc: "))
    
    print("")
    
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        print("\t\tSi a =",a,"b =",b,"y c =",c,"entonces si se puede hacer un triangulo\n")
    else:
        print("\t\tSi a =",a,"b =",b,"y c =",c,"entonces no se puede hacer un triangulo\n")

def tipoTriangulo(a, b ,c):
    
    change_Background()
    
    print("\n\t\t\t¿Se puede hacer un triangulo con los lados a, b y c?\n")
    
    a, b, c = int ( input ("\n\t\ta: ")), int ( input ("\t\tb: ")), int ( input ("\t\tc: "))
    
    print("")
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        print("\t\tSi a =",a,"b =",b,"y c =",c,"entonces si se puede hacer un triangulo\n")
        if (a == b == c):
            print("\n\t\tEquilatero\n")
        elif (a == b) or (b == c) or (a == c):
            print("\n\t\tIsosceles\n")
        else:
            print("\n\t\tEscaleno\n")
    else:
        print("\t\tSi a =",a,"b =",b,"y c =",c,"entonces no se puede hacer un triangulo\n")

def numeroPrimo(n):
    
    change_Background()
    
    print("\n\t\t\tNumeros Primos\n")

    n = int ( input ("\n\t\t\tValor(n): "))
    
    if (n%2 == 0):
        print("\n\t\t\t",n,"no es primo\n")
    else:
        print("\n\t\t\t",n,"es primo")

def validaFecha(d, m, a):
    
    calendario = [['Enero', 31], ['Febrero', 28], ['Marzo', 31], ['Abril', 30], ['Mayo', 31], ['Junio', 30], ['Julio', 31], ['Agosto', 31], ['Sepriembre', 30], ['Octubre', 31], ['Noviembre', 30], ['Diciembre', 31]]    
    
    if not ((m < 1) or (m > 12) or (a < 0)):  
        if (a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)):
            if (d > calendario[m - 1][1]) or (d < 1):   # Dies no vàlids
                if (m == 2) and (d == calendario[m - 1][1]+ 1):    # Febrer vàlid
                    my_printing(d, m, a)
                    return True   
                else:
                    print("\n¡Dias no validos!\n")
                    return False
                      
            else:
                my_printing(d, m, a)   
                return True   
        else:
            if (d > calendario[m - 1][1]) or (d < 1):   # Dies no vàlids
                print("\n¡Dias no validos!\n")
                return False
            else:
                my_printing(d, m, a)
                return True  
    else:
        print("\n¡Fecha no válida!\n")
        return False