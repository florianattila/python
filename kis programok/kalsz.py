from ipaddress import NetmaskValueError


class Szuperhos:
    def __init__(self,nev, szuperero = 50):
        self.nev = nev
        self.szuperero = szuperero

hos1 = Szuperhos("Thor", 70)
hos2 = Szuperhos("Hulk",30)

def erosebb(hos1 = Szuperhos("",0), hos2 = Szuperhos("",0)):
    if hos1.szuperero > hos2.szuperero:
        return(f"{hos1.nev} erősebb")
    else:
        return(f"{hos2.nev} erősebb")

print(erosebb(hos1, hos2))
