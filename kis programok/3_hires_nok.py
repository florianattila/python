class Hiresno:
    def __init__(self, nev, foglalkozas, nemzetiseg):
        self.nev = nev
        self.foglalkozas = foglalkozas
        self.nemzetiseg = nemzetiseg
    def elotag(self):
        if self.nemzetiseg == "a":
            return "Ms."
        else:
            return "Frau"

híres_nők = []

for _ in range(2):
    nev = input("Adja meg a nevet")
    foglalkozas = input("Adja meg a foglalkozását")
    nemzetiseg = input("Adja meg a nemzetiségét (a/n)")
    híres_nő = Hiresno(nev, foglalkozas, nemzetiseg)
    híres_nők.append(híres_nő)

for híres_nő in híres_nők:
    print(f"{híres_nő.elotag(),híres_nő.nev} egy híres {híres_nő.foglalkozas}")