import random

orzel = 0
reszka = 0
for x in range(50):
    traf = random.randint(0,1)
    if(traf==1):
        orzel+=1
    else:
        reszka+=1
print("Wylosowanych orłów: "+str(orzel))
print("Wylosowanych reszek: "+str(reszka))