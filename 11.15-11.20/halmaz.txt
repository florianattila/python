# 1)
halmaz = set([])
halmaz.clear

#2)
eredeti = set(["töltöttkrumpli, babfőzelék, tejszínes csirke"])
masolat = eredeti.copy()
print(masolat)

#3)
osztaly = set(["Gábor", "Dénes", "Juli"])
hianyzok= set(["Juli"])
jelenlevok=osztaly.difference(hianyzok)
print(jelenlevok)

#4)
szamok = set([1, 6, 8, 9, 24, 63, 74, 82, 26])
nyeroszamok = set([6, 82, 44, 16])
szamok2 = szamok.difference_update(nyeroszamok)

#5)
szamok2 = set([61, 44, 99, 63, 174, 326])
nyeroszamok2 = set([61, 82, 44, 16])
print(szamok2.intersection(nyeroszamok2)) #44, 61 (ezek vannak benne mindkettőben)

#6)
zöldség = set(["répa", "krumpli", "hagyma"])
gyümölcs = set(["alma", "körte", "barack"])
print(zöldség.intersection_update(gyümölcs))

#7)
zöldség2 = set(["répa", "krumpli", "hagyma"])
ebéd = set(["répa", "krumpli", "hagyma"])
print(zöldség.isdisjoint(gyümölcs))
#Igazat ad, ha a halmazok minden tagja különböző. Máskülönben hamisat kapunk

#8)
halmaz2 = set(["monitor", "egész", "klaviatúra", "alma"])
halmaz3 = set(["monitor", "egész", "klaviatúra"])
print(halmaz2.issubset(halmaz3))
#Ha az egyik halmaz minden eleme megegyezik a másik halmaz elemeivel akkor True-t ír ki.
#False-t akkor kapunk, ha a második halmazban hiányik az első halmaz egyik eleme

#9)
halmaz2 = set(["monitor", "egész", "klaviatúra", "alma"])
halmaz3 = set(["monitor", "egész", "klaviatúra"])
print(halmaz2.issuperset(halmaz3))
#Ha a második halmaz minden eleme megegyezik az első halmaz elemeivel akkor True-t ír ki.
#False-t akkor kapunk, ha az első halmazban hiányik a második halmaz egyik eleme.

#10)
halmaz2 = set(["monitor", "egész", "klaviatúra", "alma"])
halmaz3 = set(["monitor", "egész", "klaviatúra"])
print(halmaz2.symmetric_difference(halmaz3))
#A különbséget írja ki

#11)
járművek = set(["kolléga", "űrhajó", "autó", "bálna"]) 
járművek.discard("kolléga")
járművek.remove("bálna")
print(járművek)
járművek2 = set(["bicikli", "repülő"])
print(járművek.union(járművek2))