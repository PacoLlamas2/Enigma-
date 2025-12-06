from cargar_rotores import *

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
            print(notch)
            permutacion=input(f"Permutacio nueva para el rotor{opcion}: ")
            quieres=input("Quieres cambiar el notch? (s/n): ")
            if quieres.lower() == "s":
                notch=input("Nuevo notch: ")
            else:
                notch=notchdefecto
            print(permutacion, notch)
            
    except ValueError:
        print("Rotor no valid")

        

