print("\nPROGRESION ARITMETICA\n")
suma = 0
while True:

    terminos, desplazamiento, inicial = int ( input ("Numero de terminos: ")), int ( input ("Desplazamiento: ")), int ( input ("Numero inicial: "))

    creciente= str ( input ("¿Creciente(c) o Decreciente(d)?: "))

    if (creciente == "c") or (creciente == "C"):

        print("\nPA=",flush=True,end=" ")
        for i in range(inicial, (terminos * 2) + 2, desplazamiento):
        
            suma += i

            if (i + 2 != (terminos * 2) + 2):
                print(i,flush=True,end=", ")
            else:
                print(i,flush=True,end=" ")
        print("")
        print("\nSuma=",suma,"\n")
        break

    elif (creciente == "d") or (creciente == "D"):
        
        print("\nPA=",flush=True,end=" ")
        for i in range(inicial, (terminos * 2) + 2, -desplazamiento):
        
            suma += i

            print(i,flush=True,end=", ")

        print("")
        print("\nSuma=",suma,"\n")
        break