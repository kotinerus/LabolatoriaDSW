wartosc_w_wydmuchanym=float(input("Podaj wartość wydychanego"))
if(wartosc_w_wydmuchanym<=0.2):
    print("10 punktów karnych,\ngrzywnę od 50 zł do 5000 zł lub areszt do 30 dni,\nzakaz prowadzenia pojazdów od 6 miesięcy do 3 lat.")
elif(wartosc_w_wydmuchanym>0.2 and wartosc_w_wydmuchanym<=0.5):
    print("15 punktów karnych\nmandat w wysokości 5000 zł\nzakaz prowadzenia pojazdów od 6 miesięcy do 3 lat")
else:
    print("10 punktów karnych,\ngrzywna, która jest uzależniona od dochodów (od 10 do 540 stawek dziennych)\nsankcja od 5000 zł na rzecz Funduszu Pomocy Pokrzywdzonym oraz Pomocy Postpenitencjarnej,\nkara do 2 lat pozbawienia wolności,\zakaz prowadzenia pojazdów na minimum 3 lata.")