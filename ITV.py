eleccion = ""

while True:

    print("\nITV - GANDIA - Selecciona el tipo de vehículo\n\n\t1. ciclomotor\t4. camion\n\t2. motocicleta\t5. tractor\n\t3. coche\t6. salir")

    eleccion = int ( input ("\n\tSelecciona opcion: "))

    if (eleccion == 1):
        print("\n\tCiclomotor: 26.09€\n\tCon emisiones: 33.07\n\tSe descontará prueba ruidos (11,25€)\n")
    elif (eleccion == 2):
        print("\n\tMoto: 26.09€\n\tCon emisiones: 33.07\n\tSe descontará prueba ruidos (11,25€)\n")
    elif (eleccion == 3):
        print("\n\tTurismo gasolina no catalizado: 45,74\n\tCatalizado: 52,73\n\tTurismo diesel: 67,40\n\t(ant. 1980): 45,74\n\tSe descontará prueba ruidos (11,25€)\n")
    elif (eleccion == 4):
        print("\n\tVehículo pesado: 86,90\n\tSe descontará prueba ruidos (11,25€)\n")
    elif (eleccion == 5):
        print("\n\tTractor, maq. agrícola: 13,12\n\tSe descontará prueba ruidos (11,25€)\n")
    elif (eleccion == 6):
        print("\nFIN DEL PROGRAMA\n")
        break
    else:
        print("\nFIN DEL PROGRAMA\n")
        break

    
    eleccion = str ( input ("\n¿Quieres seguir(s)?\n"))
        
    if (eleccion == "s") or (eleccion == "S"):
        print("\nFin del programa\n")
        break
    else:
        continue