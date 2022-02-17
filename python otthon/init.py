# __init__ más nyelvekben konstruktor metodus
class Szemely:
    def __init__(self,nev,kor,nem,nemzetiseg, vallas="hindu"):
        self.nev = nev
        self.kor = kor
        self.nem = nem
        self.nemzetiseg = nemzetiseg
        self.vallas = vallas
        self.hello()

    def hello(self):
        print("hello " + self.nev)

#object instance - objektum példány
Ildi = Szemely("Ildiko",32, "no","magyar","kereszteny")
Laci = Szemely("Laszlo",42, "ferfi","orosz")
"""
print(Ildi.vallas)
print(Laci.vallas)
Ildi.hello()
Laci.hello()
"""

print(type(Ildi))

# ÖRÖKLŐDÉS
class Alkalmazott(Szemely):
    def __init__(self,nev,kor,nem,nemzetiseg, vallas, tapasztalat, megbizhatosag,vegzettseg):
        super().__init__(nev,kor,nem,nemzetiseg, vallas) #NEM KELL SELF
        self.tapasztalat = tapasztalat
        self.megbizhatosag = megbizhatosag
        self.vegzettseg = vegzettseg
        

Eni = Alkalmazott("Eniko", 25, "no", "kinai", "pogany", 2, 4, "recepcios")
print(Eni.megbizhatosag)

Kinga = Alkalmazott("Kinga", 73, "no", "magyar", "jehova", 4, 7, "konyvelo")
print(Kinga.vallas)