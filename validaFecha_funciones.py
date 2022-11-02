from funciones import *

calendario = [['Enero', 31], ['Febrero', 28], ['Marzo', 31], ['Abril', 30], ['Mayo', 31], ['Junio', 30], ['Julio', 31], ['Agosto', 31], ['Sepriembre', 30], ['Octubre', 31], ['Noviembre', 30], ['Diciembre', 31]]
change_Background()
while True:
    
    print("\n\t\t\t\tValida la fecha (12, 11, 2021)")
    
    d, m, a = int ( input("\n\t\tDia: ")), int ( input ("\n\t\tMes: ")), int ( input ("\n\t\tAño: "))
    
    if (validaFecha(d, m, a)):
        format_fecha(d, m, a, calendario)
        
        continuar = str (input ("\n¿Quieres continuar?\n"))
        
        if (continuar == "s") or (continuar == "S"):
            continue
        else:
            print("\nFIN DEL PROGRAMA\n")
            break