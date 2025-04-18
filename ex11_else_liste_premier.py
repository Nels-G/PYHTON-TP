import easygui

# Partie 1 – Recherche dans une liste
liste = [2, 5, 8, 12, 20]
n = int(easygui.integerbox("Entrez un entier à chercher dans la liste :"))

for x in liste:
    if x == n:
        easygui.msgbox(f"{n} se trouve dans la liste.")
        break
else:
    easygui.msgbox(f"{n} ne se trouve pas dans la liste.")

# Partie 2 – Test de primalité
nombre = int(easygui.integerbox("Entrez un entier positif :"))

if nombre < 2:
    easygui.msgbox("Ce n'est pas un nombre premier.")
else:
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            easygui.msgbox(f"{nombre} n’est pas premier. Premier diviseur : {i}")
            break
    else:
        easygui.msgbox(f"{nombre} est un nombre premier.")
