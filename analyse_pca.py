from scapy.all import rdpcap, UDP, IP, Raw

def analyse_pcapng(chemin_fichier):
    les_packets = rdpcap(chemin_fichier)

    dialogues = {}

    for packet in les_packets:
        if UDP in packet and (packet[UDP].sport == 9999 or packet[UDP].dport == 9999):
            ip_src = packet[IP].src
            ip_destinataire = packet[IP].dst

            dialogue_key = tuple(sorted([ip_src, ip_destinataire]))
            dialogues.setdefault(dialogue_key, []).append(packet)

    for dialogue, packets in dialogues.items():
        ip_src, ip_destinataire = dialogue

        for packet in packets:
            if Raw in packet:
                raw_data = packet[Raw].load
                first_char = chr(raw_data[0]) if raw_data else None  # Vérifie le premier caractère de raw_data
                if first_char in '01':
                    continue

                ascii_data = ''.join([chr(byte) if 32 <= byte <= 126 else '.' for byte in raw_data])
                print(f"Ascii : {ascii_data}")

                hex_data = raw_data.hex()
                print(f"Hexa : {hex_data}\n")
            else:
                print("Pas de données brutes disponibles")

chemin_fichier = 'trace_groupe_13.pcapng'
analyse_pcapng(chemin_fichier)
