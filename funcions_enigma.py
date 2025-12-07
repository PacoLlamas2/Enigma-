from files_enigma import *
from validacions import *
import variables
notchdefecto="Z"

def window_setting():
    seguir=True
    while seguir:
        con=0
        try:
            windowsel=input("Introdueix les 3 posicions de la finestra (p.ex. A B C): ")
            windowslist=windowsel.split()
            if len(windowslist) != 3:
                seguir=True
            else:
                posi = []
                for windowsstr in windowslist:
                    windowsstr=windowsstr.upper()
                    for integer, alpha in enumerate(variables.window):
                        if windowsstr == alpha:
                            posi.append(integer)
                if len(posi) != 3:
                    raise ValueError("Configuracio de la finestra no valida1")
                else:
                    print("Configuracio de la finestra validada correctament")
                    seguir=False
        except ValueError:
            print("Configuracio de la finestra no valida")
    return posi

def neteja_missatge():
    missatge=read_missatge()
    missatgesense=""
    for caracter in missatge:
        if caracter in variables.diclletres:
            missatgesense += variables.diclletres[caracter]
        else:
            missatgesense += caracter
    missatgesense=missatgesense.upper()
    missatgesep = ""
    for caracter in missatgesense:
        if caracter.isalpha(): 
            missatgesep += caracter
    missatgegrup = ""
    for i in range(0, len(missatgesep), 5):
        grup = missatgesep[i : i+5]
        missatgegrup += grup + " "
    return missatgegrup


def split_rotor():
    rotor1=carregar_rotor1()
    rotor2=carregar_rotor2()
    rotor3=carregar_rotor3()
    lineas = rotor1.split("\n")
    cablejatrotor1 = lineas[0]
    lineas = rotor2.split("\n")
    cablejatrotor2 = lineas[0]
    lineas = rotor3.split("\n")
    cablejatrotor3 = lineas[0]
    return cablejatrotor1, cablejatrotor2, cablejatrotor3
def desxifrar_missatge():
    pass

def editar_rotors(opcion):
    try:
        opcion=int(opcion)
        if opcion not in [1, 2, 3]:
            print("Rotor no valid")
        else:
            rotorfile = (f"rotor{opcion}.txt")
            con=leer_rotor(rotorfile)
            if len(con) > 1:
                notch = con[1].strip()
            else:
                notch = notchdefecto
            continuar=True
            while continuar:
                permutacio=input(f"Permutacio nova per el rotor{opcion}: ")
                try:
                    permut=permutacio.upper()
                    if len(permut) != 26 or validar_rep(permut) == False:
                        raise ValueError
                    else:
                        print("Permutacio validada correctament")
                        continuar=False
                except ValueError:
                    print("Permutacio no valida")
            quieres=input("Quieres cambiar el notch? (s/n): ")
            if quieres.lower() == "s":
                notch=input("Nou notch: ")
                notch=notch.upper()
                if len(notch) != 1:
                    raise ValueError
                else:
                    print("Notch validada correctament")
            else:
                notch=notchdefecto

            escribir_rotor(rotorfile, permut, notch)
            print("Rotor editat correctament")
            print(f"Nou contingut del rotor: {permut}, Notch: {notch}")
            
    except ValueError:
        print("Rotor no valid")

        
