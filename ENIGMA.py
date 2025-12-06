from funcions_engima import *
from cargar_rotores import *
def mostrar_menu():
    print("\nENIGMA:")
    print("-------------------------------")
    print("1. Xifrar missatge")
    print("2. Desxifrar missatge")
    print("3. Editar rotors")
    print("4. Sortir")

def main():
    seguir = True
    while seguir:
        if not carregar_rotor1() or not carregar_rotor2() or not carregar_rotor3():
            print("No s'han pogut carregar tots els rotors.")
            seguir = False
        else:
            mostrar_menu()
            opcio = input("Selecciona una opció: ")
            if opcio == '1':
                xifrar_missatge()
            elif opcio == '2':
                desxifrar_missatge()
            elif opcio == '3':
                ##EMPIEZO POR ESTE
                
                editar_rotors() 
            elif opcio == '4':
                print("Sortint...")
                seguir = False
            else:
                print("Opció no vàlida, torna-ho a provar.")

main()