import sdes as sdes
import time
import Constantes as const

# Partie 1

def str_to_dec(message):
    """ Permet de convertir un message en une liste de décimaux

    Args:
        message (str): Message à convertir

    Returns:
        list: Liste de nombres décimaux
    """
    return [ord(lettre) for lettre in message]

def chiffrement_sdes(message, cle):
    """ Permet de chiffrer un message avec SDES
    Args:
        message (str): Message à chiffrer
        cle (int): Clé de chiffrement

    Returns:
        list: Liste de nombres décimaux
    """
    liste_lettres_dec = str_to_dec(message)
    liste_dec = []
    for lettre_dec in liste_lettres_dec:
        liste_dec.append(sdes.encrypt(cle, lettre_dec))
    return liste_dec

def dechiffrement_sdes(liste, cle):
    """ Permet de déchiffrer un message avec SDES

    Args:
        liste (list): Liste de nombres décimaux du message chiffré
        cle (int): Clé de déchiffrement

    Returns:
        list: Liste de nombres décimaux
    """
    liste_dec = []
    for lettre_dec in liste:
        liste_dec.append(sdes.decrypt(cle, lettre_dec))
    return liste_dec

def chiffrement_double_sdes(message, cle1, cle2):
    """ Permet de chiffrer un message avec double SDES

    Args:
        message (str): Message à chiffrer
        cle1 (int): la clé 1
        cle2 (int): la clé 2

    Returns:
        list: Liste de nombres décimaux
    """
    liste_lettres_dec = str_to_dec(message)
    liste_dec = []
    for lettre_dec in liste_lettres_dec:
        liste_dec.append(sdes.encrypt(cle1, sdes.encrypt(cle2, lettre_dec)))
    return liste_dec

def dechiffrement_double_sdes(liste, cle1, cle2):
    """ Permet de déchiffrer un message avec double SDES

    Args:
        liste (list): Liste de nombres décimaux du message chiffré
        cle1 (int): la clé 1
        cle2 (int): la clé 2

    Returns:
        list: Liste de nombres décimaux
    """
    liste_dec = []
    for lettre_dec in liste:
        liste_dec.append(sdes.decrypt(cle2, sdes.decrypt(cle1, lettre_dec)))
    return liste_dec

def dechiffrement_double_sdes_str(liste_dec, cle1, cle2):
    """ Permet de déchiffrer un message avec double SDES et de le convertir en str

    Args:
        liste (list): Liste de nombres décimaux du message chiffré
        cle1 (int): la clé 1
        cle2 (int): la clé 2

    Returns:
        list: Liste de nombres décimaux
    """
    return "".join([chr(lettre_dec) for lettre_dec in dechiffrement_double_sdes(liste_dec, cle1, cle2)])

def cassage_brutal(message_clair, message_chiffre):
    """ Permet de casser un message chiffré avec double SDES de manière brutale

    Args:
        message_clair (str): Le message à trouver
        message_chiffre (_type_): Le message chiffré avec double SDES

    Returns:
        tuple(int, int, int): La clé 1, la clé 2 et le nombre de tentatives (nb_tentatives)
    """
    nb_tentatives = 0
    for cle1 in range(const.NOMBRE_DE_CLES_CASSAGES_SDES):
        for cle2 in range(const.NOMBRE_DE_CLES_CASSAGES_SDES):
            nb_tentatives += 1
            if dechiffrement_double_sdes_str(message_chiffre, cle1, cle2) == message_clair:
                return cle1, cle2, nb_tentatives

def cassage_astucieux(message_clair, message_chiffre):
    """ Permet de casser un message chiffré avec double SDES de manière astucieuse

    Args:
        message_clair (str): Le message à trouver
        message_chiffre (str): Le message chiffré avec double SDES

    Returns:
        tuple(int, int, int): La clé 1, la clé 2 et le nombre de tentatives (nb_tentatives)
    """
    chiffrements_intermediaires = {}
    nb_tentatives = 0
    for cle1 in range(const.NOMBRE_DE_CLES_CASSAGES_SDES):
        message_crypte = chiffrement_sdes(message_clair[:10], cle1)
        chiffrements_intermediaires[tuple(message_crypte)] = cle1
        nb_tentatives += 1
    for cle2 in range(const.NOMBRE_DE_CLES_CASSAGES_SDES):
        message_decrypte = dechiffrement_sdes(message_chiffre[:10], cle2)
        nb_tentatives += 1
        if tuple(message_decrypte) in chiffrements_intermediaires:
            return cle2, chiffrements_intermediaires[tuple(message_decrypte)], nb_tentatives
    
def string_arsene_lupin(nom_fichier):
    """ Permet de récupérer le texte d'un fichier

    Args:
        nom_fichier (str): Le nom du fichier à consulter

    Returns:
        str: Le texte du fichier
    """
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        texte_entier = fichier.read()
        lignes = texte_entier.splitlines()[2:]
        extrait = "\n".join(lignes)
        return extrait