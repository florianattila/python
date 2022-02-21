import enum


nevek = ["Andi", "Erika", "Zsofi"]
korok = [41, 12, 32]
print(list(zip(nevek, korok)))

adatok1 = {nev:kor for nev,kor in zip(nevek, korok)}
print(adatok1)

adatok2 = {"nev"+str(index+1):nev for index, nev in enumerate(nevek)}
print(adatok2)

adatok3 = {"szemely"+str(index+1):(nev,kor) for index,(nev,kor) in enumerate(zip(nevek,korok))}
print(adatok3)

adatok4 = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6}
adatok4_v2 = {k:v for k,v in adatok4.items() if v > 2 if v%2 == 0 if v%3 == 0}
print(adatok4_v2)