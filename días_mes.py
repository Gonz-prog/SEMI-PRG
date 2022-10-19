lista = ['', 'enero 31', 'febrero 28', 'marzo 31', 'abril 30', 'mayo 31', 'junio 30', 'julio 31', 'agosto 31', 'septiembre 30', 'octubre 31', 'noviembre 30', 'diciembre 31']

while True:
    
    numero = int ( input ("\nNumero del mes: "))
    
    if (numero <= 0) or (numero >= 13):
        print("\n¡Error!")
        continue
    else:
        numero_posicion = lista[numero].split()
        print("\nEl mes de",numero_posicion[0],"tiene",numero_posicion[1],"dias")

    continuar = str ( input ("\n¿Continuar(s/n)?: "))
    if (continuar == "s") or (continuar == "S"):
        continue
    else:
        print("\nFIN DEL PROGRAMA\n")
        break