# Enigma-
##Simulació Màquina Enigma

**Descripció**

Aquest projecte consisteix en una recreació de la màquina Enigma. L'Enigma era una màquina que codificava missatges utilitzant un sistema de rotors amb les lletres de l'alfabet en un ordre aleatori. S'utilitzava per a encriptar els missatges de l'exèrcit alemany, i Alan Turing va crear un dispositiu per a desencriptar els missatges xifrats amb aquesta màquina.

Aquest projecte inclou un menú interactiu per escollir entre les diferents funcionalitats:
1.***Xifrar missatge:***
- El programa demana el missatge i la posició inicial dels rotors.
- Neteja el missatge: elimina números, accents i caràcters especials.
- Agrupa les lletres resultants en **blocs de 5 lletres majúscules** separades per un espai.
- Processa el missatge pels 3 rotors. Quan un rotor arriba al seu **Notch**, fa girar el següent.
- Guarda el resultat a `data/Missatge.txt` i el mostra per pantalla.

2.***Desxifrar missatge:***
- El procés és invers al de xifratge. El missatge passa pels rotors configurats per desxifrar, recuperant el text original.
- El resultat es guarda en un arxiu `data/Xifrat.txt`.

3.***Editar rotors:***
- Permet a l'usuari editar la configuració interna dels rotors, la permutació i el notch.
- **Sistema de Validació:** Si el rotor modificat no compleix els paràmetres com lletres repetides o format incorrecte el programa avisa l'usuari i impedeix guardar l'arxiu fins que es corregeixi.
- Tots els rotors es guarden en un arxiu .txt en una carpeta especifica.

4.***Sortir:***
- Sortir del programa.

##Estructura del projecte
1.ENIGMA.py: fitxer principal del programa
2.src: carpeta on es troben els fitxers de les funcions y variables del programa
- __init__.py                   # Inicialitzador del paquet
- variables.py                  # Gestió de rutes i variables del programa
- funcions_enigma.py            # Neteja de text i lògica de les funcions del enigma
- files_enigma.py               # Gestió de lectura/escriptura d'arxius
- xifrar_enigma.py              # Algorisme de xifratge
- desxifrar_missatge.py         # Algorisme de desxifratge
- comprovar_rotores.py          # Validació inicial del sistema
- validacions.py                # Validacions amb Regex
2.config: carpeta on es troben els fitxers de configuracio dels rotors que tenen permutacio i notch
- rotor1.txt                    # Rotor 1
- rotor2.txt                    # Rotor 2
- rotor3.txt                    # Rotor 3
3.data: carpeta on es troben els fitxers de missatge i xifrat
- Missatge.txt                  # Missatge original 
- Xifrat.txt                    # Missatge xifrat per funcio xifrar_missatge
- Desxifrat.txt                 # Missatge desxifrat per funcio desxifrar_missatge
4.Readme.md: fitxer de documentacio del projecte

##Requisits
- Python 3.12.6 o superior

##Instal·lacio
- Descarregar el repositori

##Execucio
- Executar el fitxer ENIGMA.py

