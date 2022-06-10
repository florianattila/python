class Viz:
    def __init__(self, nev, kont, c):
        self.nev = nev
        self.kont = kont
        self.c = c
        self.k = self.c+273
    def hidegmeleg(self):
        if self.c >= 30:
            return "meleg"
        else:
            return "hideg"
    def halmaz(self):
        if self.c <= 0 :
            return "jég"
        elif self.c > 0:
            return "víz"
        elif self.c >= 100 :
            return "vízgőz"

folyadekok = []
for _ in range(3):
    nev = input("Adja meg a nevét!")
    kont = input("Adja meg a kontinensét!")
    hom_c = int(input("Add meg a hőmérsékletét °C-ben! "))
    viz1 = Viz(nev, kont, hom_c)
    folyadekok.append(viz1)

for x in folyadekok:
    print(f"{x.kont.lower()}i {x.nev} {x.c}°C {x.hidegmeleg()} {x.halmaz()} hőmérséklete Kelvinben: {x.k}K")