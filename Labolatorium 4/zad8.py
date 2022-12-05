working = True
while working:
    kwota = 0
    for i in range(1, 13):
        kwota += 333
        kwota = kwota + (kwota * 0.08)
        if (i == 12):
            working = False
            print("Pracownik zaoszczędzi: "+str(round(kwota))+"zł")
