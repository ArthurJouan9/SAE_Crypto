MESSAGE = '''AFXFFG XADXGFV GDFDVVVVDAFX-FVDXXFAGFAGVF XGDDGAXXADFDV GFGVVDXDVFGXF FX
VD GGGDVVXG GV VVGGGGV GAAF GVVXAVGFGG XDDFAVAF.AGGVXDG
F VGVXVGGD
VFXXFXAXDFAGGDAVG VGGG VVAXDGAGVVAGXAGFGXADGDVG:GXFXVFXDVFXDGGVGXDFG GGF V X VVGGGGD
XVAGVAVVGDFFGGXGVAG!DAGFX AFDAGFFFVAAAGGAGXVFFG!FX G DGDAG 4XDG'''

CODE = "CRYPTO"
EDOC = "CORPTY"

GRILLE = (6, 6, "AJFB82YN9UX1GS0KPI3QOE74CZVHRLT5WD6M")

def fon(mes, code):
    liste = [[] for i in range(len(code))]
    cpt = 0
    for carac in mes:
        if len(liste[cpt]) == len(mes)/len(code):
            cpt += 1
        liste[cpt].append(carac)
    return liste


message = fon(MESSAGE, EDOC)

res = ""
for j in range(48):
    res += message[0][j] + message[3][j] + message[5][j] + message[2][j] +  message[4][j] + message[1][j]

def liste_par_2(message):
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
    res = ""
    liste = liste_par_2(message)
    for double in liste:
        var = ["A", "D", "F", "G", "V", "X"]
        if double[0] in var and double[1] in var:
            indice1 = var.index(double[0])
            indice2 = var.index(double[1])

            res += GRILLE[2][indice1*GRILLE[0] + indice2]
        else:
            res += double
    return res

print(adfgvx(res))