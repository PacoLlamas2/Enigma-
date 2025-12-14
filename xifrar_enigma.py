from files_enigma import *
from funcions_enigma import *
import variables

#Funcio per calcular la entrada del rotor i la seva posicio i retornar la salida del rotor i la seva posicio
def entrada_rotor_salida(index, posi, rotor):
    indexreal = (index + posi) % 26
    for posrotor, lletrarotor in enumerate(rotor):
        if posrotor == indexreal:
            salida_rotor = variables.LLETRA_NUM[lletrarotor]
            salida_final = (salida_rotor - posi) % 26
            return salida_final
    return 0

#Funcio per formatar el xifrat i retornar-lo sense espais i en majuscules
def xifrat_format(xifrat):
    xifratambformat = ""
    for i in range(0, len(xifrat), 5):
        grup = xifrat[i : i+5]
        xifratambformat += grup + " "
    return xifratambformat

#Funcio per xifrar el missatge i retornar-lo
def xifrar_missatge(posi, missatge):
    rotor1, notch1 = pasar_rotorandnotch("rotor1")
    rotor2, notch2 = pasar_rotorandnotch("rotor2")
    rotor3, notch3 = pasar_rotorandnotch("rotor3")
    rotorlist=[rotor1, rotor2, rotor3]
    notchlist=[notch1, notch2, notch3]
    xifrat=""
    try:
        #Bucle per xifrar el missatge, lletra per lletra del missatge pasada per la funcio neteja_missatge
        for lletra in missatge:
            if lletra in variables.LLETRA_NUM:
                lletrares=variables.LLETRA_NUM[lletra]
                moviment_rotors(posi, notchlist)
                pasades=0
                while pasades < 3:
                    lletrares = entrada_rotor_salida(lletrares, posi[pasades], rotorlist[pasades])
                    pasades+=1
                lletra_cifrada = variables.NUM_LLETRA[lletrares]
                xifrat += lletra_cifrada
    except IndexError as ERRORv1:
        print(f"[ERROR] Estructura incorrecta, faltan rotors o falla la posició. Detalls: {ERRORv1}")
    except ValueError as ERRORv2:
        print(f"[ERROR] Valor buit o incorrecte de la posició. Revisa els fitxers dels rotors. Detall: {ERRORv2}")
    except Exception as ERRORv3:
        print(f"[ERROR] Error inesperat: {ERRORv3}")
    return xifrat
            
        

