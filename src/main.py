import sys
import os
from decrypt_mess1 import brute_force_caesar
from decrypt_mess2 import vigenere_decrypt, read_ciphertext
from decrypt_mess3 import fon, adfgvx

def detect_cipher_type(file_name):
    """
    Détecte le type de chiffrement à partir du nom de fichier.
    Si le fichier contient 'message1', on suppose que c'est du César,
    'message2' pour Vigenère, et 'message3' pour ADFGVX.
    """
    if 'message1' in file_name:
        return 'cesar'
    elif 'message2' in file_name:
        return 'vigenere'
    elif 'message3' in file_name:
        return 'adfgvx'
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python3 src/main.py <nom_du_fichier>")
        sys.exit(1)

    file_path = sys.argv[1]
    file_name = os.path.basename(file_path)

    cipher_type = detect_cipher_type(file_name)

    if cipher_type is None:
        print("Erreur : Impossible de déterminer le type de chiffrement à partir du nom de fichier.")
        print("Assurez-vous que le nom du fichier contient 'message1', 'message2', ou 'message3'.")
        sys.exit(1)

    if cipher_type == "cesar":
        brute_force_caesar(file_path)

    elif cipher_type == "vigenere":
        key = "CINQ"
        ciphertext = read_ciphertext(file_path)
        decrypted_message = vigenere_decrypt(ciphertext, key)
        print(f"Message déchiffré :\n{decrypted_message}")

    elif cipher_type == "adfgvx":
        MESSAGE = read_ciphertext(file_path)
        key = 'CRYPTO'
        message = fon(MESSAGE, key)
        res = ""
        for j in range(48):
            res += message[0][j] + message[3][j] + message[5][j] + message[2][j] + message[4][j] + message[1][j]
        print(adfgvx(res))

    else:
        print("Type de chiffrement non supporté.")
