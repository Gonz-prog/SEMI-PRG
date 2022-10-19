while True:
    print("\nMENU\n")
    eleccion = int ( input ("1- Progresion geometrica\n2- Serie de Fibonacci\n\nSelecciona la opcion: "))

    if (eleccion == 1):
        num_inicial, terminos, razon = int ( input ("\nNumero inicial: ")),int ( input ("\nCantidad terminos: ")),int ( input ("\nRazon: "))
        numero = num_inicial
        print(numero,flush=True,end="")
        for i in range(0, terminos - 1, 1):
            numero *= razon
            print(",",numero,flush=True,end="")
        print(" ... (num_inicial=",num_inicial,"(razon)=",razon,"terminos=",terminos)
        print("")
    
    if (eleccion == 2):
        terminos = int ( input ("\nCantidad terminos: "))
        numero = 1
        anterior = 0
        next = 1
        print(numero,flush=True,end="")
        for i in range(0, terminos - 1, 1):
            next = numero + anterior
            anterior = numero
            numero = next
            print(", ",numero,flush=True,end="")    
    break