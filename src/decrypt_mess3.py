GRILLE = (6, 6, "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M")

def fon(mes, code):
    """
    Fonction de préparation du message pour le déchiffrement ADFGVX
    """
    liste = [[] for i in range(len(code))]
    cpt = 0
    for carac in mes:
        if len(liste[cpt]) == len(mes) / len(code):
            cpt += 1
        liste[cpt].append(carac)
    return liste

def liste_par_2(message):
    """
    Sépare le message en paires de lettres
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

def adfgvx(message):
    """
    Déchiffre un message en utilisant le code ADFGVX
    """
    res = ""
    liste = liste_par_2(message)
    var = ["A", "D", "F", "G", "V", "X"]
    
    for double in liste:
        if double[0] in var and double[1] in var:
            indice1 = var.index(double[0])
            indice2 = var.index(double[1])
            res += GRILLE[2][indice1 * GRILLE[0] + indice2]
        else:
            res += double
    return res
