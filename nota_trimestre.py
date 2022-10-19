nota1 = 0
nota2 = 0
nota3 = 0
final  = 0

while nota1 == 0:
    
    nota1, nota2, nota3 = float ( input ("\nDime la nota del primer trimestre: ")), float (input("Dime la nota del segundo trimestre: ")), float (input("Dime la nota del tercer trimestre: "))

    print("\nNOTAS DEL MODULO PRG - DAW\nNota 1a evaluacion: ",nota1,"\nNota 2a evaluacion: ",nota2,"\nNota 3a evaluacion: ",nota3)
    
    final = ((nota1  + nota2) * 0.3) + (nota3 * 0.2) 
    
    if (final < 5):
        print("\nNota final: ",final,"SUSPENDIDO\n")
    elif (final >= 5) and (final < 6):
        print("\nNota final: ",final,"SUFICIENTE\n")
    elif (final >= 6) and (final < 7):
        print("\nNota final: ",final,"BIEN\n")
    elif (final >= 7) and (final < 9):
        print("\nNota final: ",final,"NOTABLE\n")
    elif (final >= 9) and (final < 10):
        print("\nNota final: ",final,"EXCELENTE\n")
    elif (final == 10):
        print("\nNota final: ",final,"SOBRESALIENTE\n")