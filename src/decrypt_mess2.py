def vigenere_decrypt(ciphertext, key):
    """
    Déchiffre un message chiffré avec le chiffrement de Vigenère en utilisant une clé donnée.
    """
    decrypted_text = []
    key_length = len(key)
    key_as_int = [ord(i) - ord('A') for i in key]  
    ciphertext_int = [ord(i) - ord('A') for i in ciphertext if i.isalpha()]  

    key_index = 0  

    for char in ciphertext:
        if char.isalpha():  
            value = (ord(char) - ord('A') - key_as_int[key_index]) % 26
            decrypted_text.append(chr(value + ord('A')))  
            key_index = (key_index + 1) % key_length  
        else:
            decrypted_text.append(char)  

    return ''.join(decrypted_text)

def read_ciphertext(file_path):
    """
    Lit le contenu d'un fichier et retourne le texte chiffré.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read().strip() 
    except FileNotFoundError:
        print(f"Erreur : le fichier '{file_path}' est introuvable.")
        sys.exit(1)
