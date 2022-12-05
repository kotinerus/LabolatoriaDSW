liczba_1=int(input("Podaj pierwszą liczbę: "))
if(liczba_1<0):
    print("Liczba jest ujemna")
else:
    print("Liczba jest dodatnia")
if(liczba_1%2!=0):
    print("Liczba jest podzielna przez 2 z resztą: "+str(liczba_1%2))
