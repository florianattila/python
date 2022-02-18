nev = None

def siker(pontszam):
    if pontszam >=48:
        return True
    else:
        return False

#siker = False
while nev != " ":
    nev = input("Adja meg a nevét! ")
    if nev:
        pontszam = int(input("Adja meg a pontot! "))
        if siker(pontszam):
            print(f"{nev} vizsgája sikeres")
            break
        else:
            print(f"{nev} vizsgája sikertelen")