from files_enigma import *
from funcions_enigma import *
import variables

def salida_rotor_entrada(index, posi, rotor, notch):
    val = (index + posi) % 26
    char = variables.NUM_LLETRA[val]
    indexreal = rotor.find(char)
    original_index = (indexreal - posi) % 26
    return original_index

def desxifrat_format(xifrat):
    xifratambformat = ""
    for i in range(0, len(xifrat), 5):
        grup = xifrat[i : i+5]
        xifratambformat += grup + " "
    return xifratambformat

def desxifrar_missatge(posi, missatge_xifrat):
    rotor1, notch1 = pasar_rotorandnotch("rotor1")
    rotor2, notch2 = pasar_rotorandnotch("rotor2")
    rotor3, notch3 = pasar_rotorandnotch("rotor3")

    rotorlist = [rotor1, rotor2, rotor3]
    notchlist = [notch1, notch2, notch3]

    text_clar = ""

    for lletra in missatge_xifrat:
        if lletra in variables.LLETRA_NUM:
            index_lletra = variables.LLETRA_NUM[lletra]

            # Avanzar rotores
            posi[0] = (posi[0] + 1) % 26
            if posi[0] == variables.LLETRA_NUM[notchlist[0]]:
                posi[1] = (posi[1] + 1) % 26
                if posi[1] == variables.LLETRA_NUM[notchlist[1]]:
                    posi[2] = (posi[2] + 1) % 26

            # Pasar por los rotores (de atrás hacia delante)
            rotor_index = 2
            while rotor_index >= 0:
                index_lletra = salida_rotor_entrada(
                    index_lletra, posi[rotor_index], rotorlist[rotor_index], notchlist[rotor_index]
                )
                rotor_index -= 1

            text_clar += variables.NUM_LLETRA[index_lletra]

    return text_clar
