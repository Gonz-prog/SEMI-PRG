lista1 = []
lista2 = []
personas = {}

while True:
    
    dni, nombre, apellido1, apellido2, edad = int (input ("\nDNI: ")), str ( input ("Nombre: ")), str ( input ("Primer apellido: ")), str ( input ("Segundo apellido: ")), int ( input ("Edad: "))

    t = (nombre+" "+apellido1+" "+apellido2, edad)
    personas[dni] = t

    continuar = str ( input ("\n¿Quieres seguir(s/n)?: "))
    
    if (continuar == "s") or (continuar == "S"):
        continue
    else:
        print("")
        for person in personas:
            print(person,'"'+personas[person][0]+'"',personas[person][1],"\n")
        
        continuar = str ( input ("\n¿Quieres volver a empezar(s/n)?: "))
    
        if (continuar == "s") or (continuar == "S"):
            continue
        else:
            print("\nFIN DEL PROGRAMA\n")
            break