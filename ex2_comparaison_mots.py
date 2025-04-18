# Sans ternaire
mot1 = input("Entrez le premier mot : ")
mot2 = input("Entrez le second mot : ")

if mot1 < mot2:
    print("Le mot le plus petit est :", mot1)
else:
    print("Le mot le plus petit est :", mot2)

# Avec ternaire
plus_petit = mot1 if mot1 < mot2 else mot2
print("Avec ternaire, le plus petit mot est :", plus_petit)
