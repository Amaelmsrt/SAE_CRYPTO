from scapy.all import *
import Fonctions_partie2 as f2
from Crypto.Cipher import AES

def dechiffrement_aes(ciphertext, key, iv):
    """ Déchiffre le texte chiffré en utilisant l'algorithme AES avec le mode CBC.

    Args:
        ciphertext (bytes): Le texte chiffré à déchiffrer.
        key (bytes): La clé de chiffrement AES.
        iv (bytes): Le vecteur d'initialisation (IV) utilisé pour le chiffrement.

    Returns:
        bytes: Le message déchiffré.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext)
    return decrypted_message

def filtrer_messages(paquets, cle):
    """ Filtrer les messages chiffrés à partir des paquets capturés.

    Args:
        paquets (List[scapy.Packet]): Liste des paquets capturés.
        cle (bytes): Clé de chiffrement AES.

    Returns:
        list: Liste des messages déchiffrés.

    """
    messages_filtres = []
    for packet in paquets:
        if packet.haslayer("UDP") and packet["UDP"].dport == 9999: # Si le paquet est un message chiffré
            iv = packet[Raw].load[:16] # Récupère le vecteur d'initialisation
            ciphertext = packet[Raw].load[16:] # Récupère le message chiffré
            message_decrypte = dechiffrement_aes(ciphertext, cle, iv)
            messages_filtres.append(message_decrypte.decode("utf-8"))
    return messages_filtres

# Charger les paquets depuis le fichier trace_sae.cap
paquets = rdpcap("./codes/trace_sae.cap")

cle = f2.trouver_cle_image("./codes/rossignol2.bmp") * 4

# Convertir la clé binaire en une clé d'octets
cle_binaire = bytes(int(cle[i:i+8], 2) for i in range(0, len(cle), 8))