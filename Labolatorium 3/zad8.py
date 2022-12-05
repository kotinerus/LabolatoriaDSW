tablica = []
for x in range(1000):
    if(not(x%2==0 or x%3==0 or x%5==0 or x%7==0)):
        tablica.append(x)
print(max(tablica))
