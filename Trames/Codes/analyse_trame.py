#!/usr/bin/env python3
"""
V2
Version Enseignant : Analyseur de trame Ethernet / IPv4 / ARP / TCP / ICMP
Affichage détaillé pas à pas avec commentaires pédagogiques.
"""

import sys

# --- Fonctions utilitaires ---
def lire_trame(fichier):
    """Lit un fichier contenant une trame hexadécimale"""
    with open(fichier, "r") as f:
        octets = []
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                octets.extend(ligne.split())
        return bytes(int(o, 16) for o in octets)


def mac_adresse(octets):
    """Convertit 6 octets en adresse MAC lisible"""
    return ":".join(f"{b:02x}" for b in octets)


def ip_adresse(octets):
    """Convertit 4 octets en adresse IP lisible"""
    return ".".join(str(b) for b in octets)


def protocole_ip(numero):
    """Retourne le nom du protocole IP"""
    mapping = {1: "ICMP", 6: "TCP", 17: "UDP"}
    return mapping.get(numero, f"Unknown ({numero})")


# --- Analyse Ethernet ---
def analyser_ethernet(trame):
    print("=== TRAME ETHERNET ===")
    dest = trame[0:6]
    src = trame[6:12]
    eth_type = trame[12:14]

    print(f"MAC destination : {mac_adresse(dest)} (6 octets)")
    print(f"MAC source      : {mac_adresse(src)} (6 octets)")
    print(f"Type Ethernet   : 0x{eth_type.hex()} (2 octets)")

    return eth_type, trame[14:]


# --- Analyse IPv4 ---
def analyser_ipv4(trame):
    print("\n=== EN-TÊTE IPv4 ===")
    version_ihl = trame[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0x0F) * 4
    total_length = int.from_bytes(trame[2:4], "big")
    ttl = trame[8]
    protocole = trame[9]
    src_ip = trame[12:16]
    dst_ip = trame[16:20]

    print(f"Version IPv4       : {version}")
    print(f"IHL (header)       : {ihl} octets")
    print(f"Longueur totale    : {total_length} octets")
    print(f"TTL                : {ttl}")
    print(f"Protocole IPv4     : {protocole} ({protocole_ip(protocole)})")
    print(f"IP source          : {ip_adresse(src_ip)}")
    print(f"IP destination     : {ip_adresse(dst_ip)}")

    payload = trame[ihl:total_length]

    # Analyse protocole supérieur
    if protocole == 1:  # ICMP
        analyser_icmp(payload)
    elif protocole == 6:  # TCP
        analyser_tcp(payload)
    else:
        print(f"\n⚠️ Protocole non supporté pour l’analyse détaillée: {protocole}")


# --- Analyse ARP ---
def analyser_arp(trame):
    print("\n=== TRAME ARP ===")
    htype = int.from_bytes(trame[0:2], "big")
    ptype = int.from_bytes(trame[2:4], "big")
    hlen = trame[4]
    plen = trame[5]
    opcode = int.from_bytes(trame[6:8], "big")
    src_mac = trame[8:14]
    src_ip = trame[14:18]
    dst_mac = trame[18:24]
    dst_ip = trame[24:28]

    print(f"Hardware type      : {htype}")
    print(f"Protocol type      : 0x{ptype:04x}")
    print(f"Hardware length    : {hlen}")
    print(f"Protocol length    : {plen}")
    print(f"Opcode             : {opcode} ({'requête' if opcode==1 else 'réponse'})")
    print(f"MAC source         : {mac_adresse(src_mac)}")
    print(f"IP source          : {ip_adresse(src_ip)}")
    print(f"MAC destination    : {mac_adresse(dst_mac)}")
    print(f"IP destination     : {ip_adresse(dst_ip)}")


# --- Analyse ICMP ---
def analyser_icmp(trame):
    print("\n=== EN-TÊTE ICMP ===")
    type_icmp = trame[0]
    code = trame[1]
    checksum = int.from_bytes(trame[2:4], "big")

    print(f"Type     : {type_icmp}")
    print(f"Code     : {code}")
    print(f"Checksum : {checksum}")


# --- Analyse TCP ---
def analyser_tcp(trame):
    print("\n=== EN-TÊTE TCP ===")
    src_port = int.from_bytes(trame[0:2], "big")
    dst_port = int.from_bytes(trame[2:4], "big")
    seq_num = int.from_bytes(trame[4:8], "big")
    ack_num = int.from_bytes(trame[8:12], "big")
    data_offset = (trame[12] >> 4) * 4
    flags = trame[13]

    print(f"Port source       : {src_port}")
    print(f"Port destination  : {dst_port}")
    print(f"Numéro de séquence: {seq_num}")
    print(f"Numéro d'ack      : {ack_num}")
    print(f"Offset header     : {data_offset} octets")
    print(f"Flags TCP         : 0x{flags:02x}")


# --- Fonction principale ---
def main():
    if len(sys.argv) != 2:
        print("Usage : python analyse_trame_enseignant.py trame.txt")
        sys.exit(1)

    trame = lire_trame(sys.argv[1])
    print(f"Lecture de la trame : {len(trame)} octets\n")

    eth_type, payload = analyser_ethernet(trame)

    if eth_type == b"\x08\x00":
        analyser_ipv4(payload)
    elif eth_type == b"\x08\x06":
        analyser_arp(payload)
    else:
        print("\n⚠️ Type Ethernet non pris en charge")


if __name__ == "__main__":
    main()