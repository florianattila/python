"""
def sikeres(nev, pont):
    if pont > 48:
        siker = True
        return f"{nev} vizsgája sikeres!", siker
    elif pont == 48:
        siker = True
        return f"{nev} éppen szerencséje van!", siker
    else:
        siker = False
        return f"{nev} vizsgája sikertelen!", siker

nev = "a"
siker = False
while nev != "":
    nev = input("Adja meg a nevet")
    pont = int(input("Adja meg a pontszamot"))
    print(sikeres(nev, pont))
    if sikeres() == True:
        break
"""

class Vizsgazo():
    def __init__(self): #Konstruktor
        self.nev = input("Adja meg a nevet")
        self.pont = int(input("Adja meg a pontszamot"))
    def sikeres(self):
        if self.pont >= 48:
            return True
        else:
            return False

diak = Vizsgazo() #Példány
print(diak.sikeres())