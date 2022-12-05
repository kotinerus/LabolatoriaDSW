tablica = []
for x in range(100, 201):
    if(not(x%6==0 or x%5==0 or x%11==0)):
        if(x%2==0):
            tablica.append(x)
print(tablica)
