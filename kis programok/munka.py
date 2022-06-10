class Szemely:
    def __init__(self, nev, kor, nem, munka):
        self.nev = nev
        self.kor = kor
        self.nem = nem
        self.munka = munka
    def neme(self):
        if self.nem == "n":
            return "hölgy"
        else:
            return "úr"
    def elotag(self):
        if self.munka == "orvos":
            return f"Dr. {self.nev}"
        else:
            return f"{self.nev}"


class Diak(Szemely):
    def __init__(self, nev, kor, nem, munka, atlag,magaviselet):
        super().__init__(nev, kor, nem, munka)
        self.atlag = atlag
        self.magaviselet = magaviselet

for _ in range(1):
    nev = input("Add meg a neved! ")
    kor = int(input("Add meg a korod! "))
    nem = input("Add meg a nemed (f/n)! ")
    munka = input("Mi a munkád? (Ha diák vagy írj egy 'D' betűt)! ")
    if munka.lower() == "d":
        atlag = float(input("Milyen átlaggal végeztél? "))
        magaviselet = int(input("Hanyas a magatartásod? "))
        szemely1 = Diak(nev, kor, nem, munka, atlag, magaviselet)
    else:
        szemely1 = Szemely(nev,kor,nem, munka)

if szemely1.munka == "d":
    print(f"{szemely1.nev} {szemely1.kor} éves, {szemely1.magaviselet} magaviselettel {szemely1.atlag} összátlaggal zárta az évet")
else:
    print(f"{szemely1.elotag()} {szemely1.neme()} {szemely1.munka}ként dolgozik, {szemely1.kor} évesen")