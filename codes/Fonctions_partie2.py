import time
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import Fonctions_partie1 as f1
from datetime import timedelta

# Partie 2

def chiffrement_aes(message, cle):
    """ Permet de chiffrer un message avec AES

    Args:
        message (str): Message à chiffrer
        cle (int): Clé de chiffrement

    Returns:
        tuple: Tuple contenant le message chiffré, le tag et le nonce
    """
    cipher = AES.new(cle, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)
    nonce = cipher.nonce
    return ciphertext, tag, nonce

def dechiffrement_aes(ciphertext, tag, cle, nonce):
    """ Permet de déchiffrer un message avec AES

    Args:
        ciphertext (str): Message chiffré
        tag (bytes): Tag de chiffrement
        cle (bytes): Clé de chiffrement
        nonce (bytes): Nonce

    Returns:
        bytes: Message déchiffré
    """
    cipher = AES.new(cle, AES.MODE_EAX, nonce=nonce)
    message = cipher.decrypt_and_verify(ciphertext, tag)
    return message


# Partie images

def trouver_bits_1(image):
    """
    Trouve les coordonnées des pixels dans l'image où le bit de poids faible est égal à 1.
    
    Args:
        image (str): Le lien de l'image à analyser.
        
    Returns:
        list: Une liste contenant les coordonnées des pixels où le bit de poids faible est 1.
    """
    i = Image.open(image)
    return [(x,y) for x in range(i.size[0]) for y in range(i.size[1]) if i.getpixel((x,y))%2 == 1], len([(x,y) for x in range(i.size[0]) for y in range(i.size[1]) if i.getpixel((x,y))%2 == 1])

def trouver_cle_image(image2):
    """ Permet de trouver la clé d'une image

    Args:
        image2 (str): Le lien de l'image à analyser

    Returns:
        str: La clé contenue dans l'image
    """
    i2 = Image.open(image2)
    cle = ""
    for x in range(64):
        cle += str(i2.getpixel((x,0))%2)
    return cle

# Calculs du temps estimé pour casser les deux chiffrements

nombre_de_cles_aes = 2**76

cles_testees_par_seconde = 10**9

temps_estime_cassage_aes = timedelta(seconds=nombre_de_cles_aes / cles_testees_par_seconde)

# print(f"Temps estimé pour casser AES : {temps_estime_cassage_aes}")