from funciones import *

change_Background()

while True:
    
    print("\n\t\tCalcular el sumatorio, productorio y valor intermedio\n\n\t\t\t\t1: Sumatorio\n\t\t\t\t2: Productorio\n\t\t\t\t3: Intermedio\n")

    n = int ( input ("\t\t\t\t"))

    if (n == 1):
        sumatorioN(n)
        continue
    if (n == 2):
        productorioN(n)
        continue
    if (n == 3):
        intermedioN(n)
        continue
    else:
        print("\n¡Error!\n")
        continue