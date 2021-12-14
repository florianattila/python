import random

szam1 = int(input("Adj meg egy számot! "))
szam2 = random.randint(10, 50)
SZAM3 = 5
print(szam1)
print(szam2)
print(SZAM3)

while szam2%2 ==1:
    szam2 = random.randint(10, 50)

if szam1%2 == 0:
    print("páros")
else:
    print("páratlan")

szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
print(szamok)
szamok.sort()
szamok.insert(1,10)
print(szamok)
szamok2 = szamok.copy()
print(szamok.count(10))
szamok.reverse()
print(szamok)