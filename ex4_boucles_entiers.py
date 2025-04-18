a = 0
b = 10

# Boucle d'incrémentation de a
while a < b:
    print("a =", a)
    a += 1

# Boucle de décrémentation de b (affiche si impair)
while b != 0:
    b -= 1
    if b % 2 != 0:
        print("b impair =", b)
