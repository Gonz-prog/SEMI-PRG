from math import sqrt

a = 1

while a != 0:

    print("\nEcuacion de 2º grado 𝑎𝑥² + 𝑏𝑥 + 𝑐 = o\n")
    a, b , c = float ( input ("Introduce a: ")),float ( input ("Introduce b: ")),float ( input ("Introduce c: "))

    positivo = -b + sqrt (b**2) - (4*a*c) / (2*a)
    negativo = -b - sqrt (b**2) - (4*a*c) / (2*a)
    print("\nSolucion 1:",positivo,"\tSolucion 2:",negativo)