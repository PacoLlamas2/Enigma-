from files_enigma import *
from funcions_enigma import *
import variables

#Funcio per calcular la entrada del rotor i la seva posicio i retornar la salida del rotor i la seva posicio
def entrada_rotor_salida(index, posi, rotor, notch):
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
    mouarotor2=False
    #Bucle per xifrar el missatge, lletra per lletra del missatge pasada per la funcio neteja_missatge
    for lletra in missatge:
        if lletra in variables.LLETRA_NUM:
            lletrares=variables.LLETRA_NUM[lletra]
            ##Condicion si la posicion del rotor1 es igual a al notch del rotor1 se mueve el rotor2
            if posi[0] == variables.LLETRA_NUM[notchlist[0]]:
                mouarotor2=True
                posi[1] = (posi[1] + 1) % 26
                ##Condicion si la posicion del rotor2 es igual a al notch del rotor2 se mueve el rotor3
                if posi[1] == variables.LLETRA_NUM[notchlist[1]]:
                    posi[2] = (posi[2] + 1) % 26
            ##MOVER EL ROTOR1-->Esto siempre se cumple
            posi[0] = (posi[0] + 1) % 26
            pasades=0
            while pasades < 3:
                lletrares = entrada_rotor_salida(lletrares, posi[pasades], rotorlist[pasades], notchlist[pasades])
                pasades+=1
            lletra_cifrada = variables.NUM_LLETRA[lletrares]
            xifrat += lletra_cifrada
    return xifrat
            
        

