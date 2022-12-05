import random
trafione = 0
losowe_numery = []
for x in range(5):
    losowe_numery.append((random.sample(range(1,42),1)))
    #losowe_numery.append(int(input("Podaj "+str(x+1)+" liczbę: ")))
print(losowe_numery)
tablica_wyników = []
for x in range(5):
    tablica_wyników.append(random.sample(range(1,42),1))
print(tablica_wyników)

for  x in range(len(losowe_numery)):
    for y in range(len(tablica_wyników)):
        if(losowe_numery[x]==tablica_wyników[y]):
            trafione+=1
print("Trafiłeś: "+str(trafione))