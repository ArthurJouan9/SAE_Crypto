import sys
import os
from decrypt_mess1 import force_brute_cesar
from decrypt_mess2 import dechiffrer_vigenere, lire_texte_chiffre
from decrypt_mess3 import preparer_message, dechiffrer_adfgvx

def detecter_type_chiffrement(nom_fichier):
    """
    Détecte le type de chiffrement à partir du nom du fichier.
    Si le fichier contient 'message1', on suppose que c'est du César,
    'message2' pour Vigenère, et 'message3' pour ADFGVX.
    """
    if 'message1' in nom_fichier:
        return 'cesar'
    elif 'message2' in nom_fichier:
        return 'vigenere'
    elif 'message3' in nom_fichier:
        return 'adfgvx'
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python3 src/main.py <nom_du_fichier>")
        sys.exit(1)

    chemin_fichier = sys.argv[1]
    nom_fichier = os.path.basename(chemin_fichier)

    type_chiffrement = detecter_type_chiffrement(nom_fichier)

    if type_chiffrement is None:
        print("Erreur : Impossible de déterminer le type de chiffrement à partir du nom de fichier.")
        print("Assurez-vous que le nom du fichier contient 'message1', 'message2', ou 'message3'.")
        sys.exit(1)

    if type_chiffrement == "cesar":
        force_brute_cesar(chemin_fichier)

    elif type_chiffrement == "vigenere":
        cle = "CINQ"
        texte_chiffre = lire_texte_chiffre(chemin_fichier)
        message_dechiffre = dechiffrer_vigenere(texte_chiffre, cle)
        print(f"Message déchiffré :\n{message_dechiffre}")

    elif type_chiffrement == "adfgvx":
        MESSAGE = lire_texte_chiffre(chemin_fichier)
        cle = 'CRYPTO'
        message_prepare = preparer_message(MESSAGE, cle)
        res = ""
        for j in range(48):
            res += message_prepare[0][j] + message_prepare[3][j] + message_prepare[5][j] + message_prepare[2][j] + message_prepare[4][j] + message_prepare[1][j]
        print(dechiffrer_adfgvx(res))

    else:
        print("Type de chiffrement non supporté.")
