import random

szam1 = int(input("írj egy számot"))
szam2 = random.randint(10,50)
SZAM3 = 5

while szam2%2 == 1: # páros vagy páratlan
    szam2 = random.randint(10,50)

if szam1%2 == 0: # páros vagy páratlan
    print("páros")
else:
    print("páratlan")

szamok = []

szamok.append(szam1) #hozzáad elemet
szamok.append(szam2) #hozzáad elemet
szamok.append(SZAM3) #hozzáad elemet
szamok.insert(2, 53)
szamok.pop(1)
print(szamok)
print(len(szamok)) #szavak/számok hossza
szamok.remove(szam1)  #eltávolít elemet
szamok.sort() #rendez
szamok.clear() #az összes elemet törli
print(szamok)

halmaz = {szam1, szam2, SZAM3}
halmaz2 = ["korte",10, szam1]
halmaz.remove(szam1) #eltávolít elemet
halmaz.add(23) #hozzáad elemet
halmaz.clear #az összes elemet törli
halmaz.discard("nem-letezo") #ha nem létezik a törölni kívánt elem nem dob vissza hibát
halmaz.pop()
print(halmaz)

with open("florianattila.txt", "w") as file:
    for item in szamok:
        file.write("%s\n" % item)


f= open("florianattila.txt")
tartalom = f.read()
print(tartalom)
f.close()

def alahuzas(strng):
    undlined = ''
    for char in strng:
        undlined += char + "---------"
    return undlined