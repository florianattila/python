#A class egy felhasználó által definiált típus
class Szemely:
    neve = ""
    kor = None
    neme = "" 
    #Methods - Metódus
    def set_kor(self, value):
        self.kor = value
    def set_nev(self, value):
        self.neve = value
    def set_nem(self, value):
        self.neme = value

sz1 = Szemely 
sz1.neve = "Ildi"
sz1.kor = 28
sz1.neme = "no"

print(sz1.neve)

sz2 = Szemely
sz2.neve = "Laci"
sz2.kor = 11
sz2.neme = "ferfi"

sz3 = Szemely() #() csak akkor kell, ha metódust használ
sz3.set_kor(21)
sz3.set_nem("no")
sz3.set_nev("Agnes")

ferenc = Szemely()
ferenc.set_kor(7)
ferenc.set_nem("ferfi")
ferenc.set_nev("Ferenc")
print(ferenc.neve)