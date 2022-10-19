while True:
    uno, dos = str ( input ("\n1a Palabra: ")), str ( input ("2a Palabra: "))
    uno_lower = uno.lower()
    dos_lower = dos.lower()

    if (uno == dos):
        print("\nLas dos palabras son exactamente iguales")
    elif (uno_lower == dos) or (uno == dos_lower):
        print("\nLas palabras son iguales (sin tener en cuenta mayusculas y minusculas)")
    elif (uno != dos) or (uno_lower != dos_lower):
        print("\nLas palabras son totalmente diferentes")
    salir = str ( input ("\n¿Quieres continuar(s/n)?: "))
    if (salir == "s") or (salir == "S"):
        continue
    else:
        print("\nFIN DEL PROGRAMA\n")
        break