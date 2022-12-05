working = True
liczby = []
while working:
    suma = 0
    srednia = 0
    liczba = int(input("Podaj liczbę: "))
    liczby.append(liczba)
    for i in range(len(liczby)):
        suma+=liczby[i]
    srednia=suma/len(liczby)
    print(srednia)
    if(liczba==0 or liczba==None): #MOŻNA WSTAWIĆ JAKIKOLWIEK ZNAK
        working=False