import random

nev = input("adja meg a nevet")
szam1 = float(input("Adj meg egy számot! "))
szam2 = random.randint(10, 50)
print(szam1)
print(szam2)
SZAM3 = 5
#halmaz
szamok2 = {}
szamok2.add(szam1)
szamok2.add(szam2)
szamok2.add(SZAM3)
#lista
szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
print(szamok)

if szam1%2 == 0:
    print("páros")
else:
    print("páratlan")