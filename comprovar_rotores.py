import os

def comprovar_rotores(): #funcion principal
    direccion = "rotores_maquina_enigma" #nombre de la carpeta
        
    try: #control de error en case de que no exista
        carpeta = os.listdir(direccion)
    except FileNotFoundError:
        print("Error: la carpeta no existe")
        return
    
    for rotor in carpeta: 
        if rotor.endswith(".txt"): #seleccion de todos los archivos txt en la carpeta
            ruta = os.path.join(direccion, rotor)
            with open (ruta, "r") as f: #abrir el archivo como lectura
                contenido_rotor = f.read().strip()
                    
                longitud_correcta = len(contenido_rotor) == 26 #comprovacion de longitud
                    
                no_caracteres_repetidos = False #comprovacion de caracteres repetidos
                verificador = ""
                    
                for letra in contenido_rotor:
                    if letra not in verificador:
                        verificador += letra
                    else:
                        break
                        
                if len(contenido_rotor) == len(verificador):
                    no_caracteres_repetidos = True
                
                if longitud_correcta and no_caracteres_repetidos: #comprovacion de parametros y informe de errores, si se encuentran
                    print(f"El rotor {rotor} es correcto\n")
                elif longitud_correcta == False:
                    print(f"Hay un error con la longitud del rotor {rotor}.\n")
                else:
                    print(f"Hay letras repetidas en el rotor {rotor}.\n")
    if len(carpeta) == 0: #si no nay archivos, informar al usuario de que esta vacio
        print("la capreta esta vacia")