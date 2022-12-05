podzielna = True
while podzielna:
    liczba = int(input("Podaj liczbę: "))
    if liczba%12==0:
        print("Podałeś liczbę podzielną przez 12, wiec kończę działanie pętli")
        podzielna=False
