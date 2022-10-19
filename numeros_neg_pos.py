from time import sleep

print("\nPROGRAMA NUMEROS")

sleep(0.8)

num = 1
positivo = 0
negativo = 0

while num != 0:
    
    num = int ( input ("Leyendo número(0 para finalizar): "))
    
    if (num < 0):
        negativo += 1
    elif (num > 0 ):
        positivo += 1

sleep(0.8)
print("\nNumeros analizados...\n")

sleep(0.8)
if (negativo >= 1):
    print("Si que hay algun numero negativo")
    sleep(0.8)
if (positivo >= 1):
    print("Total numeros positivos =",positivo)
    sleep(0.8)
if (negativo >= 1):
    print("Total numeros negativos =",negativo)
    sleep(0.8)

print("")