import sys

def dechiffrer_vigenere(texte_chiffre, cle):
    """
    Déchiffre un message chiffré avec le chiffrement de Vigenère en utilisant une clé donnée.
    """
    texte_dechiffre = []
    longueur_cle = len(cle)
    cle_int = [ord(i) - ord('A') for i in cle]  
    texte_chiffre_int = [ord(i) - ord('A') for i in texte_chiffre if i.isalpha()]  

    index_cle = 0  

    for caractere in texte_chiffre:
        if caractere.isalpha():  
            valeur = (ord(caractere) - ord('A') - cle_int[index_cle]) % 26
            texte_dechiffre.append(chr(valeur + ord('A')))  
            index_cle = (index_cle + 1) % longueur_cle  
        else:
            texte_dechiffre.append(caractere)  

    return ''.join(texte_dechiffre)

def lire_texte_chiffre(chemin_fichier):
    """
    Lit le contenu d'un fichier et retourne le texte chiffré.
    """
    try:
        with open(chemin_fichier, 'r') as fichier:
            return fichier.read().strip() 
    except FileNotFoundError:
        print(f"Erreur : le fichier '{chemin_fichier}' est introuvable.")
        sys.exit(1)
