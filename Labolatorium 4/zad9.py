import math

working = True
liczby = []
while working:
    x = int(input("Podaj liczbę: "))
    liczby.append(x)
    if len(liczby) >= 2:
        if math.fabs(liczby[-1] - liczby[-2]) < 5:
            working = False
