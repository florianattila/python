class Penz:
    def __init__(self, forint):
        self.forint = forint+ "Ft"
        self.euro = self.forint/380 , "€"
        self.font = self.forint/458 , "£"
        self.dollar = self.forint/344 , "$"
    def kiir(self):
        self.kiirforint = str(self.forint) + "Ft"
        self.kiireuro = str(self.euro) + "€"
        self.kiirfont = str(self.forint/458) , "£"
        self.kiirdollar = str(self.forint/344) , "$"

egyenleg = Penz(6000)
print(egyenleg.kiirforint)
