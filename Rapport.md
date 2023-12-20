<h1><center><span style="color:red">SAE Crypto : Défi 2</span></center></h1>

Le groupe est composé des membres suivants : 

MASERATI Amaël

GRATADE Sébastien

Groupe des membres : 

21B

# Partie 1

## Question 1 : 

Le chiffremement RSA comprend plusieurs étapes : la génération de clé, le chiffrement et le déchiffrement. La génération de clé commence par la génération de deux nombres premiers p et q aléatoires et secrets, pour ensuite pouvoir calculer leur produit nommé n. Ensuite, on calcule phi(n) que l'on nomme N, et qui correspond à l'indicatrice d'Euler de n dont le calcul est : phi(n) = (p-1)(q-1). Un entier e est ensuite choisit de sorte à ce que ce dernier et N soient premiers entre eux, ce qui correspond à PGCD(e, N) = 1. On transmet alors la clé publique RSA(e,n). Il faut par la suite calculer d, qui correspond à l'inverse modulaire de e modulo N, c'est-à-dire que si on multiplie e par d modulo N, on obtient 1. La clé privée est donc générée.

En supposant que toutes ces étapes soient correctement utilisées, Eve aura besoin d'un temps considérable pour en venir à bout car un problème intervient, qui est la factorisation de nombres premiers. En l'occurrence, Eve devra factoriser n pour pouvoir trouver p et q, ce qui est un problème difficile à résoudre. Elle aura donc énormément de mal à trouver d en testant toutes les valeurs possibles pour ce dernier.

## Retrouver des clés 

Pour retrouver des clés, il a fallu différentes étapes. Tout d'abord, il faut prendre en compte l'information donnée dans le sujet, qui est que le code de SDES ne permet d'encoder qu'un seul bloc de 8 bits, correspondant à 1 octet. Nous avons donc fait une fonction qui permet de convertir une chaîne de caractères en liste de nombres décimaux par rapport à la valeur d'une lettre en ASCII. Voici à quoi ressemble la fonction : 

![Fonction str_to_dec](./img/partie1/str_to_dec.PNG)

Ensuite, il faut faire une fonction de chiffrement SDES simple avec un message et une clé, renvoyant une liste de nombre décimaux : 

![Fonction encryptage SDES simple](./img/partie1/chiffrement_sdes.PNG)

On suit cela par une fonction de déchiffrement SDES simple avec en paramètres une liste représentant les bits du message chiffré et une clé, renvoyant à son tour une liste de nombre décimaux : 

![Fonction decryptage SDES simple](./img/partie1/dechiffrement_sdes.PNG)

On fait de même pour le chiffrement et le déchiffrement SDES double, avec les mêmes paramètres et renvoyant une liste de nombre décimaux :

![Fonction encryptage SDES double](./img/partie1/chiffrement_double_sdes.PNG)

![Fonction decryptage SDES double](./img/partie1/dechiffrement_double_sdes.PNG)

Par la même occasion, on a fait une fonction qui permet de convertir une liste de bits déchiffrés en chaîne de caractères : 

![Fonction decryptage SDES str](./img/partie1/dechiffrement_double_sdes_str.PNG)

Arrive alors la fonction qui teste toutes les possibilités de clés de déchiffrements pour retrouver un message clair à partir d'un message chiffré. Voici comment nous avons implémenté cette fonction : 

![Fonction cassage brutal](./img/partie1/cassage_brutal.PNG)

Comme méthode fonctionne, mais elle peut devenir très long selon les clés utilisées pour le chiffrement si elles sont grandes, et si le message chiffré est long aussi. Il a donc fallu trouver une méthode de cassage plus astucieuse. Voici à quoi ressemble la fonction : 

![Fonction cassage astucieux](./img/partie1/cassage_astucieux.PNG)

Cette fonction est plus rapide tout d'abord par sa complexité, qui n'utilise pas de double boucle for en O(N²) mais plutôt deux boucles for distinctes en O(N). Pour commencer, nous créons un dictionnaire qui contiendra en clé la liste des bits du message chiffré, et en valeur la clé. D'ailleurs, comme on ne peut pas mettre une liste en clé de dictionnaire avec python, nous les avons converties en tuples. Nous remplissons donc le dictionnaire avec la fonction de chiffrement SDES simple comme il n'y a qu'une clé. Lorsque le dictionnaire est complet, nous entamons notre deuxième boucle, dans laquelle nous allons tester pour chaque clé un déchiffrement SDES simple. Si le déchiffrement est présent dans les clés de chiffrement, alors nous renvoyons les clés de chiffrement et de déchiffrement correspondantes. Pour finir, pour que ça aille encore plus vite, nous avons pris en compte les dix premiers caractères du message clair et message chiffré seulement car on se dit qu'il est très fiable que lorsque les dix premières parties sont les mêmes, alors le reste le sera aussi.

Nous avons ensuite fait des tests pour comparer le cassage brutal et le cassage astucieux. Tout d'abord, on peut constater que le cassage brutal n'est pas du tout optimisé car pour des clés de 15 et 10 avec un texte assez court, il prend plus de 10 secondes à tout déchiffrer. Voici à quoi ressemble le test :

![Test cassage brutal](./img/partie1/test_cassage_brutal.PNG)
![Résultats tests cassage brutal](./img/partie1/resultats_tests_cassage_brutal.PNG)

On peut d'ailleurs constater qu'il y a eu 448 tentatives pour un nombre si petit de clés, ce qui est énorme.

Si on prend le texte du fichier fourni de l'extrait d'Arsène Lupin, le cassage astucieux prend aux alentours de moins d'une seconde à s'appliquer avec une clé de 255 et une clé de 250, ce qui est très rapide.

![Test cassage astucieux](./img/partie1/test_cassage_astucieux.PNG)
![Résultats tests cassage astucieux](./img/partie1/resultats_tests_cassage_astucieux.PNG)

Le nombre de tentatives a beau être très élevé, on peut constater que c'est extrêment rapide. Le cassage astucieux fait donc bien son travail.