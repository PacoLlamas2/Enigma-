from src.files_enigma import *
from src.funcions_enigma import *
import src.variables as variables

# Funcio que calcula el camí invers. Amb el rotor i la posicio, busca quina era l'entrada original
def salida_rotor_entrada(index, posi, rotor):
    val = (index + posi) % 26
    char = variables.NUM_LLETRA[val]
    indexreal = rotor.find(char)
    original_index = (indexreal - posi) % 26
    return original_index

#Funcio per desxifrar el missatge i retornar-lo-->Aplica el moviment dels rotors i retorna el missatge desxifrat seguint un flujo invers de R3-R2-R1
def desxifrar_missatge(posi, missatge_xifrat):
    rotor1, notch1 = pasar_rotorandnotch("rotor1")
    rotor2, notch2 = pasar_rotorandnotch("rotor2")
    rotor3, notch3 = pasar_rotorandnotch("rotor3")

    rotorlist = [rotor1, rotor2, rotor3]
    notchlist = [notch1, notch2, notch3]
    text_clar = ""
    try:
        for lletra in missatge_xifrat:
            if lletra in variables.LLETRA_NUM:
                index_lletra = variables.LLETRA_NUM[lletra]
                moviment_rotors(posi, notchlist)
                rotor_index = 2
                while rotor_index >= 0:
                    index_lletra = salida_rotor_entrada(index_lletra, posi[rotor_index], rotorlist[rotor_index])
                    rotor_index -= 1
                text_clar += variables.NUM_LLETRA[index_lletra]
    except IndexError as ERRORv1:
        print(f"[ERROR] Estructura incorrecta, faltan rotors o falla la posició. Detalls: {ERRORv1}")
    except ValueError as ERRORv2:
        print(f"[ERROR] Valor buit o incorrecte de la posició. Revisa els fitxers dels rotors. Detall: {ERRORv2}")
    except Exception as ERRORv3:
        print(f"[ERROR] Error inesperat: {ERRORv3}")
    return text_clar
