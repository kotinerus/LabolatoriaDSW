liczba_1=int(input("Podaj pierwszą liczbę: "))
liczba_2=int(input("Podaj drugą liczbę: "))
liczba_3=int(input("Podaj trzecią liczbę: "))

if(liczba_1!=liczba_2!=liczba_3):
    tablica=[liczba_1,liczba_2,liczba_3]
    makymalna=liczba_1
    minimalna=liczba_1
    for x in range(len(tablica)):
        if(makymalna<tablica[x]):
            makymalna=tablica[x]
        if(minimalna>tablica[x]):
            minimalna=tablica[x]
    print("Maksymalna: "+str(minimalna))
    print("Minimalna: "+str(makymalna))
else:
    print("Liczby są takie same")