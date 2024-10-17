GRILLE = (6, 6, "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M")

def preparer_message(message, code):
    """
    Prépare le message pour le déchiffrement ADFGVX en répartissant les caractères
    en fonction de la longueur du code.
    """
    liste = [[] for _ in range(len(code))]
    cpt = 0
    for caractere in message:
        if len(liste[cpt]) == len(message) / len(code):
            cpt += 1
        liste[cpt].append(caractere)
    return liste

def separer_par_paires(message):
    """
    Sépare le message en paires de lettres ADFGVX.
    """
    res = []
    paire = ""
    for lettre in message:
        if lettre.isalpha():
            paire += lettre
        else:
            res.append(lettre)
        if len(paire) == 2:
            res.append(paire)
            paire = ""
    return res

def dechiffrer_adfgvx(message):
    """
    Déchiffre un message en utilisant le code ADFGVX avec la grille prédéfinie.
    """
    res = ""
    liste_paires = separer_par_paires(message)
    symboles = ["A", "D", "F", "G", "V", "X"]
    
    for paire in liste_paires:
        if paire[0] in symboles and paire[1] in symboles:
            indice1 = symboles.index(paire[0])
            indice2 = symboles.index(paire[1])
            res += GRILLE[2][indice1 * GRILLE[0] + indice2]
        else:
            res += paire
    return res
