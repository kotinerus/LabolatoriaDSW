n = int(input("Podaj porządaną potęgę liczby 2: "))
liczba = 2
if(n==0):
    liczba=1
else:
    for x in range(1,n):
        liczba=liczba*2

print(liczba)