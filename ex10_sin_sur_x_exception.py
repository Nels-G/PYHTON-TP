import math

for x in range(-3, 4):
    try:
        result = math.sin(x) / x
    except ZeroDivisionError:
        result = 1  # sin(0)/0 est défini comme 1 en mathématiques
    print(f"sin({x}) / {x} = {result}")
