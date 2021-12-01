import random
nev = input("adja meg a nevet! ")
szam1 = float(input("Adj meg egy számot! "))
szam2 = random.randint(10, 50)
while szam2%2 == 1:
    szam2 = random.randint(10, 50)
print(szam1)
print(szam2)
SZAM3 = 5
#halmaz
szamok2 = {}
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


gyumolcsok = ["eper", "barack", "ananász"]
print(f"A gyümölcsök lista tartalma: {gyumolcsok}")
for (i,y) in enumerate (gyumolcsok):
    print(i,y)
print("".join(gyumolcsok))