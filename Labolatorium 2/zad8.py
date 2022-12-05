import math
dlu1=int(input("Podaj 1 bok"))
dlu2=int(input("Podaj 2 bok"))
dlu3=int(input("Podaj 3 bok"))
maks=0
tablica = [dlu1,dlu2,dlu3]
pozycja=0
for x in range(len(tablica)):
    if(maks<tablica[x]):
        maks=tablica[x]
        pozycja=x
tablica.pop(pozycja)
a_2_b_2=tablica[0]**2+tablica[1]**2
if(maks>=math.sqrt(a_2_b_2)):
    print("Trójkąt jest prostokątny")
else:
    print("Trójkąt nie jest prostokątny")

