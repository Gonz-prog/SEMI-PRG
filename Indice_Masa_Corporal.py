# Programa que pida el peso y la altura del usuario 
# para calcular el IMC - Índice de masa corporal 

# IMC = Peso (Kg) / Altura (m)²
from math import sqrt

print("\n")
print("IMC = Peso (Kg) / Altura (m)²".center(50, " "),"\n")
peso=int(input("Dime tu peso\n"))
print("\n")
altura=float(input("Dime tu altura\n"))

imc=peso/altura**2

print("\nTu IMC es",imc,"\n")