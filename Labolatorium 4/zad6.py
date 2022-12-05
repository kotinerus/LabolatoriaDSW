x=int(input("Podaj liczbę: "))
lista_dzielników = []
for i in range(1,x):
    if(x%i==0):
        lista_dzielników.append(i)
suma = sum(lista_dzielników)
if(x==suma):
    print("Liczba doskonała")