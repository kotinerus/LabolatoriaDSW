podana_liczba = int(input("Podaj ostatnia liczbę zakresu: "))
tab_pod_6_9 = []
for x in range(podana_liczba, 0, -1):
    if(x%6==0 and x%9==0):
        tab_pod_6_9.append(x)
print(tab_pod_6_9)