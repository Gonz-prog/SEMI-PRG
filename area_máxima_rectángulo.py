lado1, final = int ( input ("\nValor incial del Lado1 (x): ")),int ( input ("Valor final del Lado1 (x): "))
print("\nLado 2: 100-2x\n")
print("\nLado1(x)\tLado2(100-2x)\t(Area)")

lado2 = 100 - (2 * lado1)
lista = []
for i in range(lado1,final+1):
    print(i,"\t\t",lado2,"\t\t",i * lado2)
    lista.append(i)
    lista.append(lado2)
    lista.append(i * lado2)
    lado2 -= 2
posicion = max(lista)
total = lista.index(posicion)
numero1 = total - 1
numero2 = total - 2
total1 = lista[numero1]
total2 = lista[numero2]
print("\nEl area maxima es",max(lista),"para los lados",total2,"y",total1,"\n")