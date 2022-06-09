class Diak:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly
    def kiir(self):
        print(f"Szia, a nevem {self.nev}, és a(z) {self.osztaly} osztályba járok.")

class Tanar:
    def __init__(self, nev, szak):
        self.nev = nev
        self.szak = szak
    def kiir(self):
        print(f"Szia, a nevem {self.nev}, {self.szak} szakos tanár vagyok.")

tanar1 = Tanar("Horváth Zita", "biológia-kémia")
tanar2 = Tanar("Schmidt Edit", "matematika")
diak1 = Diak("Kiss Péter", "10.A")
tanar1.kiir()
tanar2.kiir()
diak1.kiir()