import os
#Llista de les lletres
window = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
#Diccionari per convertir les lletres accentuades en no accentuades
diclletres = {
        "á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u",
        "à": "a", "è": "e", "ò": "o", "ï": "i", "ü": "u",
        "ñ": "n", "ç": "c", 
        "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U",
        "À": "A", "È": "E", "Ò": "O", "Ï": "I", "Ü": "U",
        "Ñ": "N", "Ç": "C"
    }
# Diccionari per convertir les lletres en numeros
LLETRA_NUM = {
    "A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7,
    "I": 8, "J": 9, "K": 10, "L": 11, "M": 12, "N": 13, "O": 14, "P": 15,
    "Q": 16, "R": 17, "S": 18, "T": 19, "U": 20, "V": 21, "W": 22, "X": 23,
    "Y": 24, "Z": 25
}

# Diccionari per convertir els numeros en lletres 
NUM_LLETRA = {
    0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H",
    8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P",
    16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
    24: "Y", 25: "Z"
}
MENU_PRINCIPAL = """
ENIGMA:
-------------------------------
1. Xifrar missatge
2. Desxifrar missatge
3. Editar rotors
4. Sortir
"""
# Validem que estem en el directori correcte agafant la ruta absoluta del fitxer actual en src
DIR = os.path.dirname(os.path.abspath(__file__))
# Pugem un nivell per trobar la rel o root del projecte on esta el enigma.py 
BASE = os.path.dirname(DIR)
# Definim les rutes absolutes
Ruta_rotors = os.path.join(BASE, "config", "rotors_enigma")
Missatgefile = os.path.join(BASE, "data", "Missatge.txt")
Xifratfile = os.path.join(BASE, "data", "Xifrat.txt")
Desxifratfile = os.path.join(BASE, "data", "Desxifrat.txt")
# Noms de fitxers del rotor
rotor1 = "rotor1.txt"
rotor2 = "rotor2.txt"
rotor3 = "rotor3.txt" 
# Notch per defecte
notchdefecto = "Z" 
# Regex per validar la permutacio i el notch
REGEXpermutador = "[A-Z]{26}"
REGEXnotch = "^[A-Z]$"