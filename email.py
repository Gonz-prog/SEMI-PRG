while True:
    
    print("\nValida tu email (alumno@ieseljust.com)")
    
    e_mail = str ( input ("\nIntroduce tu email: "))

    palabras = e_mail.split("@")
    
    if (palabras[0] == " "):
        print("\n¡Error!\n")
        continue

    elif (palabras[1] == "ieseljust.com") or (palabras[1] == "hotmail.com") or (palabras[1] == "gmail.com") or (palabras[1] == "outlook.com"):
        print("\nUsuario:",palabras[0])
        print("\nServidor:",palabras[1])
        print("")
        break

    else:
        print("\nDominio no aceptado\n")
        continue