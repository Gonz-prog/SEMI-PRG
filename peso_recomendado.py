from time import sleep

sleep(0.8)
print("\nENDOCRINO - PESO RECOMENDADO - PERSONAS ADULTAS")

peso = 0

while peso == 0:
    
    peso, altura, edad = float ( input ("Introduce tu peso(kg): ")), float ( input ("Introduce tu altura(cm): ")), float ( input ("Introduce tu edad: "))

    if (peso <= 0) or (altura <= 0) or (edad <= 0):
        print("\nNo podemos hacer calculos con estos datos\n")

total = (altura-100+10%edad)*0.9

sleep(0.8)
print("\nEl peso recomendado para tu edad es:",total)

if (total > peso):
    print("Necesitas aumentar tu peso\n")
if (total == peso):
    print("¡Estas en la linea!\n")
if (total < peso):
    print("Necesitas bajar peso\n")