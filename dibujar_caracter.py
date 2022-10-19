n = 0

while n == 0:

    n, c = int ( input ("\nParametros: ")), str ( input ("Caracter: "))

    if (n == 0) or (c == ""):
        print("\nVuelve a provar\n")

print("Resultados:")

for i in range(n+1):
    print("\t\t",flush=True,end="")
    for j in range(n+1):
        print(c,flush=True,end="")
    print("")