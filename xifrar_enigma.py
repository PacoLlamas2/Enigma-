from files_enigma import *
from funcions_enigma import *
import variables


def entrada_rotor_salida(index, posi, rotor, notch):
    for posrotor, lletrarotor in enumerate(rotor):
        if posrotor == index:
            print(lletrarotor)
            salida_rotor = variables.LLETRA_NUM[lletrarotor]
            salida_final = (salida_rotor - posi) % 26
            print(salida_final)
def xifrar_missatge(posi, missatge):
    rotor1, notch1 = pasar_rotorandnotch("rotor1")
    rotor2, notch2 = pasar_rotorandnotch("rotor2")
    rotor3, notch3 = pasar_rotorandnotch("rotor3")
    print(rotor1)
    for lletra in missatge:
        if lletra in variables.LLETRA_NUM:
            print(f"La lletra {lletra} es la {variables.LLETRA_NUM[lletra]}")
            lletrares=variables.LLETRA_NUM[lletra]
            posi1=posi[0]
            #MODULO 26 para que cuando pase a la letra Z|25 vuelva a la A|0
            lletraindex=lletrares+posi1%26
            entrada_rotor_salida(lletraindex, posi1, rotor1, notch1)
        

