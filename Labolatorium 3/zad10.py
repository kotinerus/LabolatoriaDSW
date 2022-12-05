import random
wylosowane = []
for x in range(20):
    wylosowane.append(random.sample(range(1, 80),1))
wybrane_ilosc = int(input("Podaj ile chcesz wylosować liczb(1-10): "))
wybrane = []
trafione = 0
for x in range(wybrane_ilosc):
    wybrane.append(random.sample(range(1,80),1))
for i in range(len(wybrane)):
    for j in range(len(wylosowane)):
        if(wybrane[i]==wylosowane[j]):
            trafione+=1
print(trafione)

