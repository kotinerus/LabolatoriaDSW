liczba_1=float(input("Podaj pierwszą liczbę: "))
liczba_2=float(input("Podaj drugą liczbę: "))
liczba_3=float(input("Podaj trzecią liczbę: "))
liczba_4=float(input("Podaj czwartą liczbę: "))
tablica = [liczba_1,liczba_2,liczba_3,liczba_4]
najwieksza = 0
for x in range(len(tablica)):
    if najwieksza<tablica[x]:
        najwieksza=tablica[x]
print(najwieksza)
#NIGDY NIE BĘDZIE PROBLEMU