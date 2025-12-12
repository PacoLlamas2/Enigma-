import os

def comprovar_rotores():
    try:
        carpeta = "rotores_maquina_enigma"
        for rotor in os.listdir(carpeta):
            if rotor.endswith(".txt"):
                ruta = os.path.join(carpeta, rotor)
                with open (ruta, "r") as f:
                    contenido_rotor = f.read().strip()
                    longitud_correcta = len(contenido_rotor) == 26
                    no_caracteres_repetidos = False
                    verificador = ""
                    for letra in contenido_rotor:
                        if letra not in verificador:
                            verificador += letra
                        if len(verificador) == len(contenido_rotor):
                            no_caracteres_repetidos = True
                    if longitud_correcta and no_caracteres_repetidos:
                        print("El rotor es correcto\n")
                    elif longitud_correcta == False:
                        print("Hay un error con la longitud del rotor.\n")
                    else:
                        print("Hay letras repetidas en el rotor.\n")
    except FileNotFoundError:
        print("Archivo no encontrado")
    
#no completado