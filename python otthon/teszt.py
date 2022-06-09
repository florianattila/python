import random

class Kerdes:
    def __init__(self,kerdes, a, b, c, d, megoldas):
        self.kerdes = kerdes
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.megoldas = megoldas

konnyu_kerdes1 = Kerdes("Mi Görögország fővárosa?", "Athén", "Bern","Olümposz", "Ankara", "A")
konnyu_kerdes2 = Kerdes("Mi a 'pityóka' szó jelentése?", "borsó", "pálinka", "krumpli", "részeg", "C")
konnyu_kerdes3 = Kerdes("Hogy hívják a hím kacsát?", "gácsér", "gúnár", "tojó", "kakas", "A")
konnyu_kerdes4 = Kerdes("Ki volt a Legyen ön is milliomos 1. műsorvezetője?", "Fábry Sándor", "Friderikusz Sándor", "Gundel Takács Gábor", "Vágó István", "D")
konnyu_kerdes5 = Kerdes("Melyik egy nemzetközi magyar étel neve?", "kondás", "kanász", "gulyás", "juhász", "C")
konnyu_kerdes6 = Kerdes("Milyen pitypangnak hívják a gyermekláncfüvet?", "pipogya", "patyolat", "pongyola", "papucs", "C")
konnyu_kerdesek = [konnyu_kerdes1, konnyu_kerdes2, konnyu_kerdes3, konnyu_kerdes4, konnyu_kerdes5, konnyu_kerdes6]

torlesekA = ["B","C"],["B","D"],["C","D"]
torlesekB = ["A","C"],["A","D"],["C","D"]
torlesekC = ["A","B"],["A","D"],["B","D"]
torlesekD = ["A","B"],["A","C"],["B","C"]

kerdes = random.choice(konnyu_kerdesek)
if kerdes.megoldas == "A":
    torles = random.choice(torlesekA)
    print(torles)
elif kerdes.megoldas == "B":
    torles = random.choice(torlesekB)
    print(torles)
elif kerdes.megoldas == "C":
    torles = random.choice(torlesekC)
    print(torles)
elif kerdes.megoldas == "D":
    torles = random.choice(torlesekD)
    print(torles)
print(kerdes.megoldas)