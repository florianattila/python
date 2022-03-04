class Tortek:
    def kiir(self):
        print("%d/%d" % (self.szamlalo, self.nevezo), end=" ")
    """
    def beker(self):
        self.szamlalo = int(input("Kérem a számlálót"))
        self.nevezo = int(input("Kérem a nevezőt"))
    """
    def __init__(self, szamlalo, nevezo):
        self.szamlalo = szamlalo
        self.nevezo = nevezo
    def szamlalotad(self):
        return self.szamlalo
    def nevezotad(self):
        return self.nevezo

tort = Tortek(5,1)
tort.kiir()
print(tort.szamlalotad())
print(tort.nevezotad())