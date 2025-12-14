import re
import variables
def validar_rep(texto):
    llista= []
    
    for lletra in texto:
        if lletra in llista:
            raise ValueError(f"Error: La lletra {lletra} esta repetida.")
            return False
        llista.append(lletra)
    return True


def validar_permutacio(permutacio):
    validada=False
    if not re.match(variables.REGEXpermutador, permutacio) or validar_rep(permutacio) == False:
        print(f"[ERROR] Format incorrecte. S'espera 26 lletres majúscules (A-Z) sense espais ni símbols sense repetir cap lletra.")
    else:       
        validada=True
        return validada