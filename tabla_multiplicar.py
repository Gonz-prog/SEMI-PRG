from time import sleep

salida = ""

while True:
    num = int ( input ("\nTabla de multiplicar\nDime un numero\n"))
    print("\n")
    sleep(0.8)
    for i in range(1,11):
        print(num,"x",i,"=",num*i)
    print("\n")
    salida = str ( input ("¿Quieres continuar?(s/n): "))
    if (salida == "n") or (salida == "N"):
        print("\n")
        break
    elif (salida == "s") or (salida == "S"):
        print("\n")
        continue