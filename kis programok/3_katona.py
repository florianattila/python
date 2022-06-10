class Katona:
    def __init__(self, magassag, rang, nemzetiseg, nev):
        self.magassag = magassag
        self.rang = rang
        self.nemzetiseg = nemzetiseg
        self.nev = nev
    def magas(self):
        if self.magassag > 172:
            return "Elég magas"
        else:
            return "Alacsony"
    def nemzet(self):
        if self.nemzetiseg == "a":
            return "Mr"
        elif self.nemzetiseg == "n":
            return "Heer"

katonak = []

for _ in range(3):
    nev = input("Adja meg a nevét! ")
    magassag = int(input("Adja meg a magasságát cm-ben! "))
    rang= input("Adja meg a rangját")
    nemzetiseg= input("a/n? ")
    katona1 = Katona(magassag, rang, nemzetiseg, nev)
    katonak.append(katona1)

for katona in katonak:
    print(f"{katona.nemzet()} {katona.nev} eredménye: {katona.magas()}")