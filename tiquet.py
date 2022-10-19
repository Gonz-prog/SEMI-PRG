lista_producto = []
lista_precio = []
lista_cantidades = []
posicion = 0
total_final = 0
tiquet = 1

while True:
    
    print("\n")
    print("REVISAR TIQUETS DE COMPRA")
    print("-" * 50)

    producto, precio, cantidad = str ( input ("Introduce el producto: ")), float ( input ("Introduce el precio: ")), float ( input ("Introduce cantidad: "))
    
    lista_producto.append(producto)
    lista_precio.append(precio)
    lista_cantidades.append(cantidad)
    
    lineas = str ( input ("¿Mas lineas(s/n)? "))

    if (lineas == "s") or (lineas == "S"):
        continue
    else:
        print("-" * 50)
        
        print("Tiquet",tiquet)
        tiquet += 1

        print("-" * 50)
        print("PRODUCTO  "," " * 9,"PRECIO"," " * 2,"CANTIDAD"," " * 3,"TOTAL")
        print("-" * 17,"-" * 10,"-" * 10,"-" * 10)
        
        for i in range(0,len(lista_producto)):
            total = lista_precio[i] * lista_cantidades[i]
            print(lista_producto[i],flush=True,end="\t\t\t")
            print(lista_precio[i],flush=True,end="\t")
            print(lista_cantidades[i],flush=True,end="\t")
            print("{:<6.2f}".format(total),flush=True,end="\t")
            print("")
           
            total_final += total

        print("")
        print("\t\t\t\tTOTAL\t{:<6.2f}".format(total_final))
        print("-" * 50)
        continuar = str ( input ("¿Quieres continuar introduciendo tiquets?\nSI(s/S) o NO(n/N): "))

        if (continuar == "S") or (continuar == "s"):
            continue
        else:
            print("-" * 50)
            print("FIN DEL PROGRAMA\n")
            break