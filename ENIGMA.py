from src.funcions_enigma import *
from src.files_enigma import *
from src.xifrar_enigma import *
from src.desxifrar_missatge import *
from src.variables import *
from src.comprovar_rotores import *

#Funcio principal, amb el bucle per seleccionar l'opcio y executar la funcio o funcions corresponents
def main():
    if not comprovar_rotores():
        raise Exception("No s'executara el programa, comprova els rotors")
    else:
        seguir = True
        while seguir:
            print(variables.MENU_PRINCIPAL)
            opcio = input("Selecciona una opció: ")
            if opcio == "1":
                posi=window_setting()
                missatge=input("Introdueix el missatge que vols xifrar: ")
                write_missatge(variables.Missatgefile,missatge)
                missatgenet=neteja_missatge()
                xifrat=xifrar_missatge(posi, missatgenet)
                xifratambformat=xifrat_format(xifrat)
                write_missatge(variables.Xifratfile,xifratambformat)
                num_lletres = len(xifratambformat.replace(" ", "")) 
                num_grups = len(xifratambformat.split())
                print(f"[OK] Missatge xifrat a {variables.Xifratfile} ({num_lletres} lletres, {num_grups} grups de 5)")
            elif opcio == "2":
                posi=window_setting()
                mensaje=read_missatge(variables.Xifratfile)
                desxifrat=desxifrar_missatge(posi,mensaje)
                write_missatge(variables.Desxifratfile,desxifrat)
                num_lletres = len(desxifrat)
                print(f"[OK] Missatge desxifrat a {variables.Desxifratfile}: {desxifrat} ({num_lletres} lletres)")
            elif opcio == "3":
                opcion=input("Quin rotor vols editar?(1,2 o 3): ")        
                editar_rotors(opcion) 
            elif opcio == "4":
                print("Sortint...")
                seguir = False
            else:
                print("Opció no vàlida, torna-ho a provar.")

#Funcio principal
main()

