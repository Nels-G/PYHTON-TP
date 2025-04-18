while True:
    n = int(input("Entrez un entier entre 1 et 10 : "))
    if 1 <= n <= 10:
        print("Saisie correcte :", n)
        break
    else:
        print("Erreur : l'entier doit être entre 1 et 10.")
