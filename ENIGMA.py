from funcions_enigma import *
from files_enigma import *
from xifrar_enigma import *
from desxifrar_missatge import *
from variables import *
#Funcio per mostrar el menu principal
def mostrar_menu():
    print("\nENIGMA:")
    print("-------------------------------")
    print("1. Xifrar missatge")
    print("2. Desxifrar missatge")
    print("3. Editar rotors")
    print("4. Sortir")

#Funcio principal, amb el bucle per seleccionar l'opcio y executar la funcio o funcions corresponents
def main():
    seguir = True
    while seguir:
        if not carregar_rotor1() or not carregar_rotor2() or not carregar_rotor3():
            print("No s'han pogut carregar tots els rotors.")
            seguir = False
        else:
            mostrar_menu()
            opcio = input("Selecciona una opció: ")
            if opcio == "1":
                posi=window_setting()
                missatge=input("Introdueix el missatge que vols xifrar: ")
                write_missatge(variables.Missatgefile,missatge)
                missatgenet=neteja_missatge()
                xifrat=xifrar_missatge(posi, missatgenet)
                xifratambformat=xifrat_format(xifrat)
                write_missatge(variables.Xifratfile,xifratambformat)
            elif opcio == "2":
                posi=window_setting()
                mensaje=read_missatge(variables.Xifratfile)
                desxifrat=desxifrar_missatge(posi,mensaje)
                print("Missatge desxifrat: ", desxifrat)
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