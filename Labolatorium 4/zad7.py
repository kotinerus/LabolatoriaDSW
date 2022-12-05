working = True
while working:
    dzielniki = 0
    liczba = int(input("Podaj liczbę: "))
    for i in range(1,liczba):
        if(liczba%i==0):
            dzielniki+=1
    if(dzielniki<=2):
        print("Liczba jest pierrwszą")
        working=False