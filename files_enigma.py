#Funcio per carregar els rotors
def carregar_rotor1():
    try:
        with open("rotor1.txt", "r") as file1:
            cont1 = file1.read()
        return cont1
    except FileNotFoundError:
        print("El primer rotor no s'ha carregat.")

def carregar_rotor2():
    try:
        with open("rotor2.txt", "r") as file2:
            cont2 = file2.read()
        return cont2
    except FileNotFoundError:
        print("El segon rotor no s'ha carregat")

def carregar_rotor3():
    try:
        with open("rotor3.txt", "r") as file3:
            cont3 = file3.read()
        return cont3
    except FileNotFoundError:
        print("El tercer rotor no s'ha carregat.")

#Funcio per llegir el rotor
def leer_rotor(rotorfile):
    try:
        with open(rotorfile, "r") as file:
            con = file.readlines()
        return con
    except FileNotFoundError:
        print("El rotor no s'ha carregat.")

#Funcio per escriure un nou rotor amb la seva permutacio i notch
def escribir_rotor(rotorfile, permutacion, notch):
    try:
        with open(rotorfile, "w") as file:
            file.write(permutacion + "\n" + notch)
    except FileNotFoundError:
        print("El rotor no s'ha escrit.")
#Funcio per escriure el missatge normal o encriptat en un fitxer missatge.txt o xifrat.txt
def write_missatge(file,missatge):
    try:
        with open(file, "w", encoding="utf-8") as file:
            file.write(missatge)
    except FileNotFoundError:
        print("El missatge no s'ha escrit.")
#Funcio per llegir el missatge normal o encriptat de un fitxer missatge.txt o xifrat.txt
def read_missatge(file):
    try:
        with open(file, "r", encoding="utf-8") as file:
            missatge = file.read()
        return missatge
    except FileNotFoundError:
        print("El missatge no s'ha llegit.")


