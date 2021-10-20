#beágvyazott
zs = ["helló", 2.0, 5, [10,20]]
print(zs)
#lista valahanyadik elemét kiírja
szotar=["alma", "sajt", "kutya"]
print(szotar[0])
print(szotar[-3])
#a szotar elemeit kiírja számozva
for i in enumerate(szotar):
    print(i)
#a szamok lista elemeit négyzetre emeli
szamok=[4, 53]
for (i, ert) in enumerate(szamok):
    szamok[i] = ert**2
    print(szamok[i])
#listához adás
szamok.append(8)
szamok.append(56)
szamok.append(-64)
#beszúrjuk az 59-et a 3. helyre
szamok.insert(3,59)
print(szamok)
#egy a listában már létező szám beszúrása
szamok.insert(0,8)
print(szamok.count(8))
#a lista mögé bedobja
szamok.extend([44,55,66])
print(szamok)
#első 8 érték
szamok.index(56)
print(szamok)
#visszafele
szamok.reverse()
print(szamok)
#sorrend
szamok.sort()