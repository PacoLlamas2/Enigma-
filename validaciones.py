def validar_rep(texto):
    llista= []
    
    for lletra in texto:
        if lletra in llista:
            raise ValueError(f"Error: La lletra {lletra} esta repetida.")
            return False
        llista.append(lletra)
    return True