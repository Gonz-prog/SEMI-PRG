import random

lista = [0] * 5
print("\nU\t\t D\t\t C\t\t M")

for i in range(5):
    lista[i] = random.randint(1, 10)
    print(lista[i],"\t\t",lista[i] * 10,"\t\t",lista[i] * 100,"\t\t",lista[i] * 1000)