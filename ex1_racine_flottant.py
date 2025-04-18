import math

x = float(input("Entrez un nombre flottant : "))

if x >= 0:
    print("La racine carrée est :", math.sqrt(x))
else:
    print("Erreur : le nombre est négatif.")
