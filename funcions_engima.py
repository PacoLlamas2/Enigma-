from cargar_rotores import *
from validaciones import *
notchdefecto="Z"
def xifrar_missatge():
    pass

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

        
