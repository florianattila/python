import random

#változók definiálása
neme = None
vizsgalt = ["Zsolt", "Vivien", "Juli", "Eduárdó"]
fiuk= ["Zsolt", "Gábor", "Péter", "Eduárdó"]
lanyok = ["Anna", "Vivien", "Maja", "Juli"]
jatek = ["dob", "PS4", "gyertya", "kisautó"]
ajandek = random.choice(jatek)
nev = input("Adja meg a nevet!")
#eljárás
def mi_a_neme(nev):
    if nev in fiuk:
        nem = "fiu"
    elif nev in lanyok:
        nem = "lany"
    else:
        print("Nem tudom a nemet")

"""
lista = ["egyik elem", "másik elem"]
vizsgált = "harmadik elem"
if vizsgált in lista:
    print("benne van")
else:
    ("Nincs benne")
"""

if nev in fiuk:
    nem = "fiu"
elif nev in lanyok:
    nem = "lany"
else:
    print("Nem tudom a nemet")

mi_a_neme(nev)

if nev in vizsgalt:
    print("Nem kap játékot")
else:
    if nem == "lany":
        print("Lányos játék")
    elif nem == "fiu":
        print("fiús játék")
    
print(f'{nev} {jatek}-t kap.')