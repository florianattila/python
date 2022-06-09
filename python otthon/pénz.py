class Penz:
    def __init__(self, huf):
        self.huf = huf
        self.euro = huf/380
        self.font = huf/460
        self.dollar = huf/342
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Penz(self.huf + other)
    def kiir(self, value):
        if value == "huf":
            return f"{self.huf}ft"
        elif value == "euro":
            return f"{self.euro:.3f}€"
        elif value == "font":
            return f"{self.font:.3f}£"
        elif value == "dollar":
            return f"{self.dollar:.3f}$"

asd2 = 200
asd = Penz(asd2)
print(f"Az egyenlege:\n {asd.kiir('huf')} \n {asd.kiir('euro')} \n {asd.kiir('font')} \n {asd.kiir('dollar')}")