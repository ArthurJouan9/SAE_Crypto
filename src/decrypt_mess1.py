def cesar_dechiffre(texte_chiffre, decalage):
    """
    Déchiffre un message chiffré avec le chiffrement de César en fonction du décalage fourni.
    Seules les lettres majuscules sont déchiffrées, les autres caractères restent inchangés.
    """
    texte_dechiffre = ''
    for caractere in texte_chiffre:
        if caractere.isalpha() and caractere.isupper():
            base = ord('A') 
            caractere_dechiffre = chr((ord(caractere) - base - decalage) % 26 + base)
            texte_dechiffre += caractere_dechiffre
        else:
            texte_dechiffre += caractere
    return texte_dechiffre

def force_brute_cesar(chemin_fichier):
    """
    Tente de déchiffrer un message chiffré avec un chiffrement de César en essayant tous les décalages possibles (1 à 25).
    """
    try:
        with open(chemin_fichier, 'r') as fichier:
            message_chiffre = fichier.read().strip()

        print(f"Message chiffré : {message_chiffre}")
        print("\nTentatives de déchiffrement :\n")

        for decalage in range(1, 26):
            message_dechiffre = cesar_dechiffre(message_chiffre, decalage)
            print(f"Décalage {decalage} :\n{message_dechiffre}\n")

    except FileNotFoundError:
        print(f"Erreur : le fichier '{chemin_fichier}' est introuvable.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
