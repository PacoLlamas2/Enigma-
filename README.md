#Simulación Máquina Enigma

##Descripción
Este proyecto consiste en una recreación de la máquina enigma. 
La enigma era una máquina que codificava mensajes utilizando un 
sistema de rotores con las letras del lafabeto en un orden aleatorio. 
Se utilizaba para encriptar los mensajer del ejercito alemán y 
Alan Turing crea un dispositivo para desencriptar los mensajes cifrados
con esta máquina.

Este proyecto incluye un menu para escojer la funcionalidad, las cuales
incluyen codificar, decodificar, y modificar los rotores de la máquina enigma.
También hay una función para salir del programa.

Para codificar el mensaje, el programa pedirá al usuario el mensaje que quiera 
encriptar, el cual guarda en un documento .txt, y la posición inicial del rotor.
entonces, pasará el mensaje a un formato sin números, acentos, ni carácteres 
especiales y agrupara las letras restantes en grupos de 5 letras mayusculas 
separadas por un espacio. 
Después, pasará el mensaje por los rotores para codificar el mensaje. 
Por cada letra que pase por el rotor, este avanzará una letra hasta 
llegar al notch, el cual hará girar el siguiente rotor, cambiando la letra de esta.
Este proceso se repite hasta que todos las las letras del mensaje hayan 
pasado por el rotor. Y entonces, el programa guarda el mensaje cifrado en 
un documento .txt y muestra el mensaje cifrado.

El proceso de descifrado es igual al proceso de cifrado, solo que el mensaje 
passa por el rotor, el cual gira al revés, y decodifica el mensaje, muestra el mensaje
decodificado, y lo guarda en un archivo .txt.

Los archivos .txt en el que estan guardados el mensaje original y el mensaje encriptado
solo guardaran los mensajes más recientes.

La función de modificar rotores permite al usuario modificar los rotores de la máquina
enigma. La función pregunta al usuario por el rotor que quiere modificar y entonces
abre el archivo .txt en el que esta guardado el rotor y permite al usuario editarlo.
Si después de la modificación el rotor no cumple con los parámetros, entonces el programa
avisa al usuario sobre la parte que no cumple el rotor modificado y le pide volver a 
modificar el rotor hasta que el rotor modificado cumpla con los parametros.

Todos los rotores se guardan en un archivo .txt en una carpeta especifica.