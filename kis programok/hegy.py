class Hegy:
    def __init__(self, nev= "", magassag= 0):
        self.nev = nev
        self.magassagm = magassag
        self.magassagkm = self.magassagm/1000
    def kiir(self):
        print(f"A {self.nev} nevű hegy {self.magassagm}m ({self.magassagkm:.2f}km) magas")

hegy1 = Hegy("")
hegy2 = Hegy("")
def beker():
    hegy_nev = input("Kérem a hegy nevét")
    hegy_magassag = int(input("Kérem a hegymászó magasságát"))
    hegy1 = Hegy(hegy_nev, hegy_magassag)
    hegy_nev = input("Kérem a hegy nevét")
    hegy_magassag = int(input("Kérem a hegymászó magasságát"))
    hegy2 = Hegy(hegy_nev, hegy_magassag)
    return hegy1, hegy2

def magasabb(hegy1 = Hegy("",0), hegy2=Hegy("",0)):
    if hegy1.magassagm > hegy2.magassagm:         
        print(f"a(z) {hegy1.nev} magasabb")
    else:
        print(f"A {hegy2.nev} magasabb")

magasabb(beker())
hegy1.kiir()
