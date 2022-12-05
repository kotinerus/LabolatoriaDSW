liczby = []
working = True
while working:
    suma = 0
    srednia = 0
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)
    suma=sum(liczby)
    srednia = suma/len(liczby)
    print(suma)
    print(srednia)
    if(suma>100 or srednia==66):
        working=False