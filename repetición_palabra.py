cadena="manzana|pera|manzana|cereza|pera|manzana|pera|pera|cereza|pera|fresa"

lista = []
nocopy = []

palabras = list(cadena.split("|"))

for i in palabras:

    if i not in nocopy:
        nocopy.append(i)
        contar = []
        contar.append(i)
        contar.append(palabras.count(i))
        añadir = tuple(contar)
        lista.append(añadir)


print("\n",lista)

for i in lista:

    print("\nLa",i[0],"está presente",i[1],"veces")
print("")