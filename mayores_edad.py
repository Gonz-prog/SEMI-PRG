lista_nombres = []
lista_edades = []
lista_final = []

while True:

    nombre = str ( input ("\nNombre o (-) para finalizar: "))

    if (nombre == "-"):
        break
    edad = int ( input ("Edad: "))
    if (edad >= 18):
        lista_nombres.append(nombre)
        lista_edades.append(edad)
        continue
    
continuar = str ( input ("\n¿Imprimir resultados(s/n)?: "))
if (continuar == "s") or (continuar == "S"):
    print("\nAlumnos mayores de edad:",flush=True,end=" ")

    for i, j in zip(lista_nombres,lista_edades):
        print(i,j,flush=True,end=" ")

    primer_mayor = max(lista_edades)
    posicion_1 = lista_edades.index(primer_mayor)

    lista_final.append(lista_nombres[posicion_1])
    lista_final.append(lista_edades[posicion_1])

    lista_nombres.pop(posicion_1)
    lista_edades.pop(posicion_1)

    segundo_mayor = max(lista_edades)
    posicion_2 = lista_edades.index(segundo_mayor)

    lista_final.append(lista_nombres[posicion_2])
    lista_final.append(lista_edades[posicion_2])
    
    print("")
    print("\nLos dos alumnos mayores:",lista_final[0],lista_final[1],"y",lista_final[2],lista_final[3])
    print("\nFIN DEL PROGRAMA\n")

else:
    print("\nFIN DEL PROGRAMA\n")