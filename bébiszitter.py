"""
lista = ["egyik elem", "másik elem"]
vizsgált = "harmadik elem"
if vizsgált in lista:
    print("benne van")
else:
    ("Nincs benne")
"""

nev = input("Adja meg a nevet!")
nem = None

vizsgalt = ["Zsolt", "Vivien", "Juli", "Eduárdó"]
fiuk= ["Zsolt", "Gábor", "Péter", "Eduárdó"]
lanyok = ["Anna", "Vivien", "Maja", "Juli"]
"""
def mi_a_neme(nev):
    if nev in fiuk:
        nem = "fiu"
    elif nev in lanyok:
        nem = "lany"
    else:
        print("Nem tudom a nemet")
mi_a_neme(nev)
"""
if nev in fiuk:
    nem = "fiu"
elif nev in lanyok:
    nem = "lany"
else:
    print("Nem tudom a nemet")
print(nem)

if nev in vizsgalt:
    print("Már meg lett vizsgálva")
else:
    if nem == "lany":
        print("Lányos játék")
    elif nem == "fiu":
        print("fiús játék")
