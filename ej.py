from trivial_function import *
change_Background()
print(
    "\t\t\t\t\t\t$$$$$$$\  $$\   $$\  $$$$$$\        $$$$$$$\  $$\        $$$$$$\ $$\    $$ \ \n"
    "\t\t\t\t\t\t$$  __$$\ $$ |  $$ |$$  __$$\       $$  __$$\ $$ |      $$  __$$\\$$\    $$ |\n"
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ /  $$ |      $$ |  $$ |$$ |      $$ /  $$ |\$$\ $$ /\n"
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$$$$$$  |$$ |      $$$$$$$$ | \$$$$ /\n"
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$  ____/ $$ |      $$  __$$ |  \$$ /\n" 
    "\t\t\t\t\t\t$$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |      $$ |      $$ |  $$ |   $$ |\n"  
    "\t\t\t\t\t\t$$$$$$$  |\$$$$$$  | $$$$$$  |      $$ |      $$$$$$$$\ $$ |  $$ |   $$ |\n"   
    "\t\t\t\t\t\t\_______/  \______/  \______/       \__|      \________|\__|  \__|   \__|\n"
)
# \n\t\t\t\t\t\t\t\t
pregunta = 0
puntos = 0
preguntas = (("¿Cual fue el apellido de casada de la premio Nobel Marja Sklodowska?"), ("Curie"), ("¿Contra que dos selecciones campeonas del mundo jugó España en el Mundial 82?"), ("Contra Alemania e Inglaterra"), ("¿Cuantas patas tiene un octopodo?"), ("Ocho"), ("¿Quien fue el primer Jefe de Estado tras la muerte de Franco?"), ("Juan Carlos I"), ("¿En que año tuvieron lugar los primeros Juegos Olimpicos disputados en España?"), ("1992"), ("¿Con que otro nombre tambien se llaman los quebrados?"), ("Fracciones"), ("¿Cual es el musculo mas rapido del cuerpo humano?"), ("El parpado"), ("¿Quien fue el primer presidente de los Estados Unidos?"), ("George Washington"), ("¿En que region francesa se desarrollo la herejia catara?"), ("En el Langueduc"), ("¿Que organos del cuerpo humano expulsan dioxido de carbono?"), ("Los pulmones"), ("¿Los atletas de que pais llevan impresa en sus camisetas la palabra Helas?"), ("Los de Grecia"), ("¿Qien fue el primer europero que visito las islas Hawai?"), ("James Cook"), ("¿Que pierde un amnesico?"), ("La memoria"), ("¿En que deporte olimpico no se admite el profesionalismo y es obligatorio el casco?"),("En boxeo"), ("¿Cuantas horas marca al dia un reloj digital?"),("24"), ("¿Quien fue la ultima reina de Egipto?"),("Cleopatra"), ("¿Cual es la ciudad que tiene en su escudo un oso y un madroño?"), ("Madrid"), ("¿Quien sobrevivio del Septimo de Caballeria del general Custer en Little Bighorn?"), ("Un caballo"), ("¿Que ingenio a vapor se invento en 1925?"), ("La locomotora"), ("¿Cual fue el equipo italiano de Ronaldo?"),("Inter de Milan"), ("¿En que cuarto de la casa se coloca el papel mas higienico?"), ("En el cuarto de baño"), ("¿En que pais actual habria nacido el mariscal Tito?"), ("En Croacia"), ("¿De que pais europeo depende la Alsacia?"), ("De Alemania"), ("¿De que color es la franja que llevan los taxis madrileños?"), ("Roja"), ("¿Quen fue el primer rey de Israel?"), ("Saul"), ("¿Que presidente italiano pidio a sus futbolistas Vencer o Morir?"), ("Benito Mussolini"), ("¿Como se llaman los deportistas que juegan con cesta?"), ("Pelotarias"), ("¿Que presidente norteamericano dio cia libre a la Guerra del Golfo?"), ("George Bush"), ("¿Cual es el vaile trípico de Galicia?"), ("La Muñeira"), ("¿En que pais no necesitas ponerte chulo para hablar flamenco?"), ("En Belgica"), ("¿En que pais se pueden encontrar mas monjes budistas?"), ("En el Tibet"), ("¿En que pais americano se invento el padel?"), ("En Mejico"), ("¿Que son el <<tornado>> y el <<star>>?"), ("Enbarcaciones olimpicas"), ("¿Cual es la Ciudad Imperial?"), ("Toledo"), ("¿En que oceano esta la isla de Diego Garcia?"),("En el Indico"), ("¿En que continente esta el Valle del Rif?"), ("En Africa"), ("¿Como se llamaba anteriormente Lefkosia?"), ("Nicosia"), ("¿A que ciclista español le llamaron EL Extraterrestre?"),("A Miguel Indurain"), ("¿Que capital de provincia es famosa por sus burgas?"), ("Ourense"), ("¿En que pais se encuentra el desierto de Kalahari?"), ("En Australia"), ("¿Cual es el volcan en activo mas alto de Europa?"), ("El Etna"), ("¿Cual es la capital de provincia catalana que cambio su nombre?"), ("Girona"), ("¿Que lago asturiano esta mas proximo al Ercina?"), ("El Enol"), ("¿Que es un polvo en Galicia?"), ("Un pulpo"), ("¿En que archipielago esta la isla Graciosa?"), ("En Canarias"), ("¿Quien fue el primer navegante europeo que llego por mar a la India?"), ("Vasco de Gama"))

total = int ( input ("\n\t\t\t\t\t\t\t\t¿Cuantas preguntas quieres responder\n\t\t\t\t\t\t\t\t?"))

for i in range(total):
    print("\n\t\t\t\t\t\t\t\t",preguntas[pregunta])
    
    respuesta = str ( input ("\n\t\t\t\t\t\t\t\t"))
