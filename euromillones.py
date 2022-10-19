from random import shuffle


lista = [1, 2, 3, 4, 5, 6 ,7, 8, 9 ,10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40 ,41, 42, 43, 44, 45]
lista2 = [1, 2, 3, 4, 5]
print("")
for i in range(5):
    shuffle(lista)
    print("Numeros",lista[0])
print("")
for j in range(2):
    shuffle(lista2)
    print("Estrellas",lista2[0])