from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def binaire_to_octet(chaineBinaire):
    """
    Convertit une chaîne binaire en octets.
    """
    return int(chaineBinaire, 2).to_bytes((len(chaineBinaire) + 7) // 8, byteorder='big')

def decryptage_cbc(vecteur_init, cle, message_chiffre):
    """
    Déchiffre un message chiffré en AES-256 en mode CBC.
    - vecteur_init: vecteur d'initialisation (IV) de 16 octets
    - cle: clé de 32 octets (256 bits)
    - message_chiffre: message chiffré (doit être un multiple de 16 octets)
    """
    if len(vecteur_init) != 16:
        raise ValueError("Le vecteur d'initialisation (IV) doit faire 16 octets.")
    if len(message_chiffre) % 16 != 0:
        raise ValueError("La longueur du message chiffré doit être un multiple de 16 octets.")
    if len(cle) != 32:
        raise ValueError("La clé AES-256 doit faire 32 octets (256 bits).")
    
    chiffre = Cipher(algorithms.AES(cle), modes.CBC(vecteur_init), backend=default_backend())
    decodeur = chiffre.decryptor()
    message_clair = decodeur.update(message_chiffre) + decodeur.finalize()
    return message_clair

if __name__ == "__main__":
    cles_binaire = "0100000000110010100010000001000000111000010011001001111000101110111110010011000101100011111011100110001000110010000111011010101110110100101000001111011100011000100111011010010000010001111111011000110110001011000110111011101111110110001000111011110111010111011000101001011101011011110001010011011011000100101011001000110001000111011001110010110101110011111100110100110100111100101000101101111011111100110000000101011000011100100010101110100110001111011000110011000100110000111110010100011011110001100011000100111011001011001100011011100001001000100010001100100001111100100100111000100110100100110011110110101100100010110100100101011011011101110001100101101000010001101101110111110100100011101111010000110110000101001100100110000110001010100111101011010001010101011111100110010110111011111101110000110100111111100111011110010111000101100001001111110010001110010110001000100100111100011110111000100010111000011000101011000111000110110010110100110100000010001001101000010001000011001100000101001110111000000111000110110101100110"
    
    cle1 = cles_binaire[:256]
    cle2 = cles_binaire[256:512]
    cle3 = cles_binaire[512:768]
    cle4 = cles_binaire[768:1024]

    cle_bytes1 = binaire_to_octet(cle1)
    cle_bytes2 = binaire_to_octet(cle2)
    cle_bytes3 = binaire_to_octet(cle3)
    cle_bytes4 = binaire_to_octet(cle4)

    cles = [
        cle_bytes1, 
        cle_bytes2, 
        cle_bytes3, 
        cle_bytes4
    ]

    messages = [
        bytes.fromhex("f98c2d0a255231d90975c5eff450689f35f73ec4545d67790c1c080b38c63dbb804ca272117b955f52e1c361d77256f7"),
        bytes.fromhex("ad68c62560748c0a9f8cd64fc299d377321107a667bb4d3c9274d920b54e48e9804ca272117b955f52e1c361d77256f7"),
        bytes.fromhex("e4c708c39971973f77b16652c51300034d6c8ad14a0c3fed8006a1f9fa3ef187a80c00f219e50e041073251f7f3d7201"),
        bytes.fromhex("7dea7b5dc8785cd153cc189a64e546128c351fe6929c362abb363c250a190647a80c00f219e50e041073251f7f3d7201")
    ]

    for index, message in enumerate(messages, start=1):
        vecteur_init = message[:16]
        texte = message[16:]
        
        print(f"\n======= Test des 4 clés sur le message {index} =======")
        for i, cle in enumerate(cles, start=1):
            print(f"Tentative de déchiffrement avec la clé {i} :")
            try:
                message_dechiffre = decryptage_cbc(vecteur_init, cle, texte)
                print(f"Message déchiffré avec clé {i} : {message_dechiffre}\n")
            except ValueError as e:
                print(f"Erreur de déchiffrement avec clé {i} : {e}\n")
