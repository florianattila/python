class Allatfaj:
    def __init__(self, fajnev, tomeg = 0):
        self.fajnev = fajnev
        self.tomeg = tomeg
    def kiir():
        print(f"A(z) {self.fajnev} állat {self.tomeg} tömegű")

allatfajok = []
for _ in range(3):
    allatfaj = input("Allat neve")
    allattomeg = int(input("allat tomege"))
    allat = Allatfaj(allatfaj, allattomeg)
    allatfajok.append(allat)

legnehezebb = allatfaj(0)

for allatfaj in allatfajok:
    if allatfaj.tomeg > legnehezebb.tomeg:
        legnehezebb.tomeg = allatfaj.tomeg
print(f"A legnehezebb állat a {legnehezebb.fajnev} ")
