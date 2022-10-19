from random import shuffle

lista = ["1","X","2"]
num = 0
while True:
    for i in range(1,9999):
        print("\n",i,"a quiniela\n")
        for j in range(1,16):
            shuffle(lista)
            print("Posicion",j,":",lista[0])
    
        if (j == 15):
            salida = str ( input ("\n¿Quieres continuar(intro)? Salir(s).\n"))

            if (salida == "S") or (salida == "s"):
                break
            else:
                continue