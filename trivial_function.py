from time import sleep
from os import system
from operator import __name__
from random import randint

def titol():
    
    print(
        "\t\t\t$$$$$$$$\         $$\            $$\           $$\       $$$$$$$\                                          $$\   $$\   \n"  
        "\t\t\t\__$$  __|        \__|           \__|          $$ |      $$  __$$\                                         \__|  $$ | \n"   
        "\t\t\t   $  | $$$$$$\   $$\ $$\    $$\ $$\  $$$$$$\  $$ |      $$ |  $$ |$$\   $$\  $$$$$$\   $$$$$$$\ $$\   $$\ $$\ $$$$$$\   \n"
        "\t\t\t   $$ | $$  __$$\ $$ |\$$\  $$  |$$ | \____$$\ $$ |      $$$$$$$  |$$ |  $$ |$$  __$$\ $$  _____|$$ |  $$ |$$ |\_$$  _|  \n"
        "\t\t\t   $$ | $$ |  \__|$$ | \$$\$$  / $$ | $$$$$$$ |$$ |      $$  ____/ $$ |  $$ |$$ |  \__|\$$$$$$\  $$ |  $$ |$$ |  $$ |    \n"
        "\t\t\t   $$ | $$ |      $$ |  \$$$  /  $$ |$$  __$$ |$$ |      $$ |      $$ |  $$ |$$ |       \____$$\ $$ |  $$ |$$ |  $$ |$$\ \n"
        "\t\t\t   $$ | $$ |      $$ |   \$  /   $$ |\$$$$$$$ |$$ |      $$ |      \$$$$$$  |$$ |      $$$$$$$  |\$$$$$$  |$$ |  \$$$$  |\n"
        "\t\t\t   \__| \__|      \__|    \_/    \__| \_______|\__|      \__|       \______/ \__|      \_______/  \______/ \__|   \____/\n"
        "\n\n"
        "\t\t\t\t\t\t\t\t\t\t\t\t|             ,---.                    |         \n"
        "\t\t\t\t\t\t\t\t\t\t\t\t|---.,   .    |  _.,---.,---.,---,,---.|    ,---.\n"
        "\t\t\t\t\t\t\t\t\t\t\t\t|   ||   |    |   ||   ||   | .-' ,---||    |   |\n"
        "\t\t\t\t\t\t\t\t\t\t\t\t`---'`---|    `---'`---'`   ''---'`---^`---'`---'\n"
        "\t\t\t\t\t\t\t\t\t\t\t\t     `---'                                     \n\n"
    )

def solo_titol():
    
    print(
    "\t\t\t\t\t $$$$$$\   $$$$$$\  $$\       $$$$$$\        $$$$$$$\  $$\        $$$$$$\ $$\     $$\ \n"
    "\t\t\t\t\t$$  __$$\ $$  __$$\ $$ |     $$  __$$\       $$  __$$\ $$ |      $$  __$$\\$$\   $$  |\n"
    "\t\t\t\t\t$$ /  \__|$$ /  $$ |$$ |     $$ /  $$ |      $$ |  $$ |$$ |      $$ /  $$ |\$$\ $$  /\n" 
    "\t\t\t\t\t\$$$$$$\  $$ |  $$ |$$ |     $$ |  $$ |      $$$$$$$  |$$ |      $$$$$$$$ | \$$$$  /\n"  
    "\t\t\t\t\t \____$$\ $$ |  $$ |$$ |     $$ |  $$ |      $$  ____/ $$ |      $$  __$$ |  \$$  /\n"   
    "\t\t\t\t\t$$\   $$ |$$ |  $$ |$$ |     $$ |  $$ |      $$ |      $$ |      $$ |  $$ |   $$ |\n"    
    "\t\t\t\t\t\$$$$$$  | $$$$$$  |$$$$$$$$\ $$$$$$  |      $$ |      $$$$$$$$\ $$ |  $$ |   $$ |\n"    
    "\t\t\t\t\t \______/  \______/ \________|\______/       \__|      \________|\__|  \__|   \__|\n"
    )

def duo_titol():
    print(
    "\t\t\t\t\t\t$$$$$$$\  $$\   $$\  $$$$$$\        $$$$$$$\  $$\        $$$$$$\ $$\     $$\ \n"
    "\t\t\t\t\t\t$$  __$$\ $$ |  $$ |$$  __$$\       $$  __$$\ $$ |      $$  __$$\\$$\   $$  |\n"
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ /  $$ |      $$ |  $$ |$$ |      $$ /  $$ |\$$\ $$  /\n"
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$$$$$$  |$$ |      $$$$$$$$ | \$$$$  /\n"
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$  ____/ $$ |      $$  __$$ |  \$$  /\n" 
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |      $$ |      $$ |  $$ |   $$ |\n"  
    "\t\t\t\t\t\t$$$$$$$  |\$$$$$$  | $$$$$$  |      $$ |      $$$$$$$$\ $$ |  $$ |   $$ |\n"   
    "\t\t\t\t\t\t\_______/  \______/  \______/       \__|      \________|\__|  \__|   \__|\n"
)

def menu():
    print("\n\t\t\t\t\t\t\t\t1. Jugadores\n\t\t\t\t\t\t\t\t2. Dificultad\n\t\t\t\t\t\t\t\t3. Jugar Partida\n\t\t\t\t\t\t\t\t4. Salir\n")

def clear():
    
    if __name__ == 'nl':
        system("cls")
    else:
        system("clear")

def change_Background():
    
    print("\033[1;32;40m")
    
    clear()

def partida_solo(preguntas, respuestas, lista_puntos_solo):
    
    solo_titol()
    puntos = 0
    pregunta = randint(0, 32)
    total = int ( input ("\n\t\t\t\t\t\t\t\t¿Cuantas preguntas quieres responder?\n\t\t\t\t\t\t\t\t"))

    for i in range(total):
        print("\n\t\t\t\t\t\t\t\t",preguntas[pregunta])

        respuesta = str ( input ("\n\t\t\t\t\t\t\t\t"))

        if (respuesta == respuestas[pregunta]):
            print("\n\t\t\t\t\t\t\t\tRespuesta correcta")
            puntos += 1
            pregunta += 2
        else:
            print("\n\t\t\t\t\t\t\t\t¡Respuesta incorrecta!")
            pregunta += 2
    print("\n\t\tPuntos:",puntos)
    lista_puntos_solo.append(puntos)
    
    sleep(3)
    
def partida_duo(preguntas, respuestas, lista_puntos_duo):
    
    duo_titol()
    pregunta = randint(0, 32)
    puntos1 = 0
    puntos2 = 0
    
    total = int ( input ("\n\t\t\t\t\t\t\t\t¿Cuantas preguntas quiere responder cada jugador?\n\n\t\t\t\t\t\t\t\t"))

    for i in range(total):
        
        print("\n\t\t\t\t\t\t\t\tPregunta para el Jugador 1\n\t\t\t\t\t\t\t\t",preguntas[pregunta])
        
        respuesta = str ( input ("\n\t\t\t\t\t\t\t\t"))
        if (respuesta == respuestas[pregunta]):
            print("\n\t\t\t\t\t\t\t\tRespuesta correcta")
            puntos1 += 1
            pregunta += 2
        else:
            print("\n\t\t\t\t\t\t\t\tRespuesta incorrecta")
            pregunta += 2
        
        print("\n\t\t\t\t\t\t\t\tPregunta para el Jugador 2\n\t\t\t\t\t\t\t\t",preguntas[pregunta])
        
        respuesta2 = str ( input ("\n\t\t\t\t\t\t\t\t"))
        if (respuesta2 == respuestas[pregunta]):
            print("\n\t\t\t\t\t\t\t\tRespuesta correcta")
            puntos2 += 1
            pregunta += 2
        else:
            print("\n\t\t\t\t\t\t\t\tRespuesta incorrecta")
            pregunta += 2

    print("\n\t\tPuntos\n\t\tJugador 1:",puntos1,"\n\t\tJugador 2:",puntos2)
    lista_puntos_duo.append("Jugador 1")
    lista_puntos_duo.append(puntos1)
    lista_puntos_duo.append("Jugador 2")
    lista_puntos_duo.append(puntos2)
    sleep(3)