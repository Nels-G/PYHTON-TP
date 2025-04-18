pSeuil = 2.3
vSeuil = 7.41

pression = float(input("Entrez la pression actuelle : "))
volume = float(input("Entrez le volume actuel : "))

if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat ! Pression et volume dépassent les seuils.")
elif pression > pSeuil:
    print("Attention : augmenter le volume de l’enceinte.")
elif volume > vSeuil:
    print("Attention : diminuer le volume de l’enceinte.")
else:
    print("Tout va bien.")
