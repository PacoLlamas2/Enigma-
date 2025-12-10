from files_enigma import *
from validacions import *
import variables
notchdefecto="Z"


#Funcio per configurar la finestra, validarla i retornar la posicio de les 3 finestres
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

#Funcio per netejar el missatge i retornar-lo sense espais, punts i comes i en majuscules, també retorna el missatge sense grups de 5
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

#Funcio per separar el rotor en cablejat 
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

#Funcio per separar el rotor en cablejat i notch
def split_rotor_notch():
    rotors = [carregar_rotor1(), carregar_rotor2(), carregar_rotor3()]
    cablejatlist = []
    notchelist = []
    for rotor in rotors:
        #Separar el texto en líneas
        lineas = rotor.strip().splitlines()
        # lineas[0] es la cadena o primera linea del rotor
        cablejatlist.append(lineas[0].strip())
        # lineas[1] es el notch
        if len(lineas) > 1:
            notchelist.append(lineas[1].strip())
        else:
            notchelist.append("Z") 
    return cablejatlist, notchelist

#Funcio per seleccionar el rotor i la seva posicio
def pasar_rotorandnotch(rotorsel):
    cablejatlist, notchelist = split_rotor_notch()
    if rotorsel == "rotor1":
        return cablejatlist[0], notchelist[0]
    elif rotorsel == "rotor2":
        return cablejatlist[1], notchelist[1]
    elif rotorsel == "rotor3":
        return cablejatlist[2], notchelist[2]
    else:
        raise ValueError("Rotor no valid")

#Funcio per seleccionar el rotor i la seva posicio<--MIRAR FUNCIONALITAT
def rotor(index, posi, rotor):
    for posrotor, lletrarotor in enumerate(rotor):
        print((posrotor, lletrarotor))

#Funcio per editar els rotors i la seva posicio ademes de validar la configuracio
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

        
