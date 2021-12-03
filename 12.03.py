import random

szam1 = int(input("Kérek egy számot"))
szam2 = random.randint(10, 50)
SZAM3 =  5

while szam2%2 == 1:
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
print(szamok)
szamok.reverse()
print(szamok)
print(type(szamok))
print(len(szamok))
szamok.remove(5)
print(szamok)

szamok2 = {}