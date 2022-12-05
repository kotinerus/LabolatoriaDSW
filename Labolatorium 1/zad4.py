from datetime import datetime

godzina_na_sekundy=3600
print("Godzina to: "+str(1*godzina_na_sekundy)+"s")

doba_na_sekunde=godzina_na_sekundy*24
print("Dzień to: "+str(1*doba_na_sekunde)+"s")

rok_na_sekunde=doba_na_sekunde*365
print("Rok to: "+str(1*rok_na_sekunde)+"s")

now = datetime.now()
lata=(int(now.strftime("%Y"))-2002)*rok_na_sekunde
miesiecy=(int(now.strftime("%m"))-6)*30.5*doba_na_sekunde
dni=(int(now.strftime("%d"))-3)*doba_na_sekunde
now_hr=now.strftime("%H")
now_min=now.strftime("%M")
now_s=now.strftime("%S")
dzis=int(now_hr)*3600+int(now_min)*60+int(now_s)
czas_zycia=int(lata+miesiecy+dni+dzis)

print("Czas życia: "+str(czas_zycia)+"s")
