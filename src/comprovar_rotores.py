import os
import src.variables as var 
from src.files_enigma import *
from src.validacions import *
from src.funcions_enigma import *
def comprovar_rotores():
    #Comprobacio que la carpeta de rotrs existeix
    try: 
        if os.path.exists(var.Ruta_rotors):
            carpeta=os.listdir(var.Ruta_rotors)
            if (var.rotor1 in carpeta) and (var.rotor2 in carpeta) and (var.rotor3 in carpeta):
                print("[OK] Tots els rotors estan disponibles")
            else:
                raise FileNotFoundError("Un o més rotors no estan disponibles") 
        else:
            raise FileNotFoundError("La carpeta no existeix")
        
    except Exception as error:
        print(f"[ERROR] {error}")
        return False
    try:
        for rotor in carpeta:
            contingut=leer_rotor(rotor)
            permutacio_notch=processar_dades_rotor(contingut)
            if not permutacio_notch:
                raise ValueError(f"Contingut buit del {rotor}")
            else:
                if validar_permutacio(permutacio_notch[0]) and validar_notch(permutacio_notch[1]):
                    print(f"[OK] El {rotor.split('.')[0]} es correcte")
                else:
                    raise ValueError(f"El {rotor.split('.')[0]} no es correcte")
        return True
    except Exception as error:
        print(f"[ERROR] {error}")
        return False
    