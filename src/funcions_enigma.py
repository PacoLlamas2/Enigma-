from src.files_enigma import *
from src.validacions import *
import src.variables as variables

#Funcio per configurar la finestra, validarla i retornar la posicio de les 3 finestres
def window_setting():
    seguir=True
    while seguir:
        con=0
        try:
            windowsel=input("Introdueix les 3 posicions de la finestra en format correcte amb espais entre elles (p.ex. A B C): ")
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
    missatge=read_missatge(variables.Missatgefile)
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


def processar_dades_rotor(rotor):
    try:
        llista = []
        if len(rotor) > 0:
            rotor=rotor[0].strip()
            llista.append(rotor)
        else:
            raise ValueError("No hi ha cap permutacio")
        if len(rotor) > 1:
            rotor=rotor[1].strip()
            llista.append(rotor)
        else:   
            llista.append(variables.notchdefecto)
        return llista
    except Exception as error:
        print(f"[ERROR] {error}")
    
#Funcio per seleccionar el rotor i la seva posicio
def rotor(index, posi, rotor):
    for posrotor, lletrarotor in enumerate(rotor):
        print((posrotor, lletrarotor))

#Funcio per moviment dels rotors i la seva posicio
def moviment_rotors(posi, notchlist):
    try:
        #Condicio si la posicio del rotor1 es igual al notch del rotor1, es mou el rotor2
        mover_rotor2 = (posi[0] == variables.LLETRA_NUM[notchlist[0]])
        # Condicio si el rotor 3 es te que moure
        # Nomes si el rotor 2 es mura i ademes si adems el rotor2 esta en el seu notch
        mover_rotor3 = False
        if mover_rotor2:
            if posi[1] == variables.LLETRA_NUM[notchlist[1]]:
                mover_rotor3 = True
        # Aplicar el moviment dels rotors
        if mover_rotor3:
            posi[2] = (posi[2] + 1) % 26
        if mover_rotor2:
            posi[1] = (posi[1] + 1) % 26
        #MOVER EL ROTOR1-->Esto siempre se cumple
        posi[0] = (posi[0] + 1) % 26

        return posi
    except IndexError as ERRORv1:
        print(f"[ERROR] {ERRORv1}")
    except ValueError as ERRORv2:
        print(f"[ERROR] {ERRORv2}")
    except Exception as ERRORv3:
        print(f"[ERROR] {ERRORv3}")

#Funcio per editar els rotors i la seva posicio ademes de validar la configuracio
def editar_rotors(opcion):
    try:
        #Demana quin rotor vols editar i valida que sigui un rotor valid entre el rotor 1, rotor 2 i rotor 3
        opcion=int(opcion)
        #Si el rotor no es valid, torna-ho a provar
        if opcion not in [1, 2, 3]:
            print("Rotor no valid")
        else:
            #Si l'opcio es valida, crea una variable per llegir el rotor
            rotorfile = (f"rotor{opcion}.txt")
            con=leer_rotor(rotorfile)
            #Si el rotor te notch, ho guarda, si no, el notch sera "Z"
            if len(con) > 1:
                notch = con[1].strip()
            #Crea una variable per la permutacio i valida que sigui una permutacio valida
            continuar=True
            while continuar:
                permutacio=input(f"Permutacio nova per el rotor{opcion}: ")
                try:
                    permut=permutacio.upper().strip()
                    if not validar_permutacio(permut):
                        raise ValueError
                    else:
                        print("Permutacio validada correctament")
                        continuar=False
                except ValueError:
                    print("Permutacio no valida")
            #Si vols canviar el notch, demana el nou notch i valida que sigui un notch valid
            quieres=input("Quieres cambiar el notch? (s/n): ")
            if quieres.lower() == "s":
                notch=input("Nou notch: ")
                notch=notch.upper().strip()
                if len(notch) != 1 and not notch.isalpha():
                    raise ValueError
                else:
                    print("Notch validada correctament")
            else:
                notch=variables.notchdefecto   
            #Escriu el rotor amb la nova permutacio i el nou notch
            escribir_rotor(rotorfile, permut, notch)
            print(f"[OK] Rotor editat correctament: {permut}, Notch: {notch}")
    except ValueError:
        print("[ERROR] L'opció introduïda no és un número.")
    except Exception as e:
        print(f"[ERROR] Ha fallat l'edició del rotor: {e}")

        
