#!/usr/bin/env python3
"""
V2
Analyseur de trame réseau super détaillé pour enseignant
Affiche trame hex + ASCII, offsets, Ethernet / IPv4 / ARP / TCP / ICMP
Idéal pour projection et correction de TP
"""

import sys

# --- Utilitaires ---
def lire_trame(fichier):
    with open(fichier, "r") as f:
        octets = []
        for ligne in f:
            ligne = ligne.strip()
            if ligne:
                octets.extend(ligne.split())
        return bytes(int(o, 16) for o in octets)

def mac_adresse(octets):
    return ":".join(f"{b:02x}" for b in octets)

def ip_adresse(octets):
    return ".".join(str(b) for b in octets)

def protocole_ip(numero):
    mapping = {1:"ICMP",6:"TCP",17:"UDP"}
    return mapping.get(numero, f"Unknown ({numero})")

def afficher_hexa_ascii(trame):
    print("\n=== TRAME COMPLETE HEX + ASCII ===")
    for i in range(0, len(trame), 16):
        bloc = trame[i:i+16]
        hex_str = " ".join(f"{b:02x}" for b in bloc)
        ascii_str = "".join(chr(b) if 32 <= b <= 126 else "." for b in bloc)
        print(f"{i:04x}  {hex_str:<48}  {ascii_str}")

# --- Analyse Ethernet ---
def analyser_ethernet(trame):
    print("\n=== EN-TÊTE ETHERNET ===")
    dest = trame[0:6]
    src = trame[6:12]
    eth_type = trame[12:14]
    print(f"MAC destination : {mac_adresse(dest)}")
    print(f"MAC source      : {mac_adresse(src)}")
    print(f"Type Ethernet   : 0x{eth_type.hex()}")
    return eth_type, trame[14:]

# --- Analyse IPv4 ---
def analyser_ipv4(trame):
    print("\n=== EN-TÊTE IPv4 ===")
    version_ihl = trame[0]
    version = version_ihl >> 4
    ihl = (version_ihl & 0x0F) * 4
    total_length = int.from_bytes(trame[2:4],"big")
    ttl = trame[8]
    proto = trame[9]
    src_ip = trame[12:16]
    dst_ip = trame[16:20]

    print(f"Version      : {version}")
    print(f"IHL          : {ihl} octets")
    print(f"Total Length : {total_length}")
    print(f"TTL          : {ttl}")
    print(f"Protocole    : {proto} ({protocole_ip(proto)})")
    print(f"IP source    : {ip_adresse(src_ip)}")
    print(f"IP dest      : {ip_adresse(dst_ip)}")

    payload = trame[ihl:total_length]
    if proto == 1:
        analyser_icmp(payload)
    elif proto == 6:
        analyser_tcp(payload)
    else:
        print(f"⚠️ Protocole non pris en charge pour détails: {proto}")

# --- Analyse ARP ---
def analyser_arp(trame):
    print("\n=== EN-TÊTE ARP ===")
    htype = int.from_bytes(trame[0:2], "big")
    ptype = int.from_bytes(trame[2:4], "big")
    hlen = trame[4]
    plen = trame[5]
    opcode = int.from_bytes(trame[6:8], "big")
    src_mac = trame[8:14]
    src_ip = trame[14:18]
    dst_mac = trame[18:24]
    dst_ip = trame[24:28]
    print(f"Opcode           : {opcode} ({'requête' if opcode==1 else 'réponse'})")
    print(f"MAC source       : {mac_adresse(src_mac)}")
    print(f"IP source        : {ip_adresse(src_ip)}")
    print(f"MAC destination  : {mac_adresse(dst_mac)}")
    print(f"IP destination   : {ip_adresse(dst_ip)}")

# --- Analyse ICMP ---
def analyser_icmp(trame):
    print("\n=== EN-TÊTE ICMP ===")
    type_icmp = trame[0]
    code = trame[1]
    checksum = int.from_bytes(trame[2:4],"big")
    print(f"Type     : {type_icmp}")
    print(f"Code     : {code}")
    print(f"Checksum : {checksum}")

# --- Analyse TCP ---
def analyser_tcp(trame):
    print("\n=== EN-TÊTE TCP ===")
    src_port = int.from_bytes(trame[0:2],"big")
    dst_port = int.from_bytes(trame[2:4],"big")
    seq = int.from_bytes(trame[4:8],"big")
    ack = int.from_bytes(trame[8:12],"big")
    offset = (trame[12] >> 4)*4
    flags = trame[13]
    print(f"Port source      : {src_port}")
    print(f"Port dest        : {dst_port}")
    print(f"Numéro séquence  : {seq}")
    print(f"Numéro ack       : {ack}")
    print(f"Offset header    : {offset} octets")
    print(f"Flags TCP        : 0x{flags:02x}")

# --- Tableau résumé ---
def tableau_resume(trame):
    print("\n=== TABLEAU RESUME DES CHAMPS ===")
    eth_type = trame[12:14]
    print(f"{'Champ':<25} {'Valeur'}")
    print("-"*50)
    print(f"{'MAC dest':<25} {mac_adresse(trame[0:6])}")
    print(f"{'MAC src':<25} {mac_adresse(trame[6:12])}")
    print(f"{'Type Ethernet':<25} 0x{eth_type.hex()}")
    if eth_type==b"\x08\x00":
        version_ihl = trame[14]
        version = version_ihl>>4
        ihl = (version_ihl &0x0F)*4
        total_length = int.from_bytes(trame[16:18],"big")
        proto = trame[23]
        src_ip = trame[26:30]
        dst_ip = trame[30:34]
        print(f"{'IPv4 Version':<25} {version}")
        print(f"{'IHL':<25} {ihl}")
        print(f"{'Total Length':<25} {total_length}")
        print(f"{'Protocole':<25} {proto} ({protocole_ip(proto)})")
        print(f"{'IP source':<25} {ip_adresse(src_ip)}")
        print(f"{'IP destination':<25} {ip_adresse(dst_ip)}")
    elif eth_type==b"\x08\x06":
        opcode = int.from_bytes(trame[20:22],"big")
        print(f"{'Opcode ARP':<25} {opcode}")
        print(f"{'MAC src ARP':<25} {mac_adresse(trame[22:28])}")
        print(f"{'IP src ARP':<25} {ip_adresse(trame[28:32])}")
        print(f"{'MAC dst ARP':<25} {mac_adresse(trame[32:38])}")
        print(f"{'IP dst ARP':<25} {ip_adresse(trame[38:42])}")

# --- Main ---
def main():
    if len(sys.argv)!=2:
        print("Usage: python analyse_trame_superdetail.py trame.txt")
        sys.exit(1)

    trame = lire_trame(sys.argv[1])
    print(f"Trame lue : {len(trame)} octets")
    afficher_hexa_ascii(trame)
    eth_type, payload = analyser_ethernet(trame)
    if eth_type==b"\x08\x00":
        analyser_ipv4(payload)
    elif eth_type==b"\x08\x06":
        analyser_arp(payload)
    else:
        print("⚠️ Type Ethernet non supporté")
    tableau_resume(trame)

if __name__=="__main__":
    main()