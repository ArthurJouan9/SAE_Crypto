# ADFGVX
# CrÃ©Ã© par ChatGPT, corrigÃ© et amÃ©liorÃ© par Didier MÃ¼ller

import math


# Fonction pour crÃ©er la grille de substitution ADFGVX avec un alphabet personnalisÃ©
# Le rÃ©sultat est un dictionnaire
def create_adfgvx_square(custom_alphabet):
    if len(custom_alphabet) != 36:
        raise ValueError("L'alphabet personnalisÃ© doit contenir exactement 36 caractÃ¨res.")
    adfgvx = "ADFGVX"
    square = {}
    idx = 0
    for i in adfgvx:
        for j in adfgvx:
            square[custom_alphabet[idx]] = i + j
            idx += 1
    return square


# Fonction pour crÃ©er la permutation d'aprÃ¨s un mot-clef
def create_permut(keyword):
    alphabet2= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    tab = []
    nbiter = len(keyword)
    for m in range(nbiter):
        rang = 1000
        for n in range(nbiter):
            ch = keyword[n]
            if alphabet2.index(ch) < rang:
                j = n + 1
                ok = True
                for r in range(m):
                    ok = ok and (j != tab[r])
                if ok:
                    rang = alphabet2.index(ch)
                    k = j
        tab.append(k)
    for j in range(nbiter):
        tab[j] -= 1
    return tab



# Fonction pour inverser la grille de substitution
def invert_square(square):
    return {v: k for k, v in square.items()}






# Fonction de dÃ©chiffrement
def decrypt(ciphertext, permutation, square):
    # Retirer les espaces pour obtenir le texte chiffrÃ© original
    ciphertext = ciphertext.replace(' ', '')

    num_cols = len(permutation)
    num_rows = math.ceil(len(ciphertext) / num_cols)

    # Calculer la longueur des colonnes
    col_lengths = [len(ciphertext) // num_cols] * num_cols
    for i in range(len(ciphertext) % num_cols):
        col_lengths[i] += 1

    # Initialiser les colonnes en utilisant la permutation inverse
    columns = [''] * num_cols
    start = 0
    for index in range(num_cols):
        col_index = permutation[index]
        col_len = col_lengths[col_index]
        columns[col_index] = ciphertext[start:start + col_len]
        start += col_len

    # Construire le texte transposÃ©
    transposed_text = ''
    for i in range(num_rows):
        for col in columns:
            if i < len(col):
                transposed_text += col[i]

    # Remplacer les paires par les lettres correspondantes
    inv_square = invert_square(square)
    plaintext = ''.join(inv_square[transposed_text[i:i+2]] for i in range(0, len(transposed_text), 2))
    return plaintext


# Exemple d'utilisation
custom_alphabet = "c1ofwjymt5b4i7a28sp30qhxkeul6dvrgzn9".upper()  # Exemple d'alphabet personnalisÃ©
square = create_adfgvx_square(custom_alphabet)
print("Grille de substitution:", square)
permutation = create_permut("CRYPTO")
# ou, si l'on veut, on peut aussi directement Ã©crire la permutation : permutation = [1, 3, 4, 5, 0, 2]
print("Permutation:", permutation)
print()



encrypted = "AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF .AGGVXDG F VGVXVGGD VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG "

decrypted = decrypt(encrypted, permutation, square)
print("Message dÃ©chiffrÃ©:", decrypted)

