# Programa que pregunte por la base y la altura de un triángulo y muestre por
# pantalla el área de ese triángulo
import datetime
 
today = datetime.datetime.today()
print(f"{today:%d %B, %Y}")

base=int(input("\nDime la base del triangulo:\n"))
altura=int(input("Dime la altura del triangulo\n"))

area=base*altura

print("El area del triangulo es",area)