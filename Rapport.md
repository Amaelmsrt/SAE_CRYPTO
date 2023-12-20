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
