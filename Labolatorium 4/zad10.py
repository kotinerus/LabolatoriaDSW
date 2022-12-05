working  = True
liczby = []
while working:
    x = int(input("Podaj liczbę: "))
    liczby.append(x)
    print(sum(liczby))
    if(len(liczby)>=2):
        if(liczby[-1]==liczby[-2]):
            working=False