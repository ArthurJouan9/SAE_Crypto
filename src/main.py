import sys

def caesar_decrypt(ciphertext, shift):
    """
    Déchiffre un message crypté avec le chiffrement de César en fonction du décalage fourni.
    Seules les lettres majuscules sont déchiffrées, les autres caractères restent inchangés.
    """
    decrypted_text = ''
    for char in ciphertext:
        if char.isalpha() and char.isupper():
            shift_base = ord('A') 
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

def brute_force_caesar(file_path):
    """
    Tente de déchiffrer un message crypté avec un chiffrement de César en essayant tous les décalages possibles (1 à 25).
    """
    try:
        with open(file_path, 'r') as file:
            encrypted_message = file.read().strip()

        print(f"Message crypté : {encrypted_message}")
        print("\nTentatives de déchiffrement :\n")

        for shift in range(1, 26):
            decrypted_message = caesar_decrypt(encrypted_message, shift)
            print(f"Décalage {shift} : {decrypted_message}")

    except FileNotFoundError:
        print(f"Erreur : le fichier '{file_path}' est introuvable.")
    except Exception as e:
        print(f"Une erreur est survenue : {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation : python3 main.py <nom_du_fichier>")
        sys.exit(1)

    file_path = sys.argv[1]

    brute_force_caesar(file_path)



