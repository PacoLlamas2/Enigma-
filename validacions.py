import re
import variables
def validar_rep(texto):
    try:
        llista=[]
        for lletra in texto:
            if lletra in llista:
                raise ValueError(f"Error: La lletra {lletra} esta repetida.")
                return False
            llista.append(lletra)
        return True
    except Exception as error:
        print(f"[ERROR] {error}")
        return False
    

def validar_permutacio(permutacio):
    try:
        validada=False
        if not re.match(variables.REGEXpermutador, permutacio) or validar_rep(permutacio) == False:
            print(f"[ERROR] Format incorrecte. S'espera 26 lletres majúscules (A-Z) sense espais ni símbols sense repetir cap lletra.")
        else:       
            validada=True
            return validada
    except Exception as error:
        print(f"[ERROR] {error}")
        return False

def validar_notch(notch):
    try:
        if re.match(variables.REGEXnotch, notch) and len(notch) == 1:
            return True
        else:
            raise ValueError(f"[ERROR] El notch ha de ser una única lletra majúscula entre A i Z. Valor rebut: {notch}")    
    except Exception as error:
        print(f"[ERROR] {error}")
        return False