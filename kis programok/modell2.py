wr = open("modell2.txt", "w")

kor = int(input("Adja meg az életkorát "))
nev = input("Adja meg a nevét ")
magassag = int(input("Adja meg a magasságát "))

def modell_kor(kor):
    if kor < 20:
        return "Ez a modell még csitri"
    elif kor > 20:
        return "Ez a modell vén"
    else:
        return modell_magassag(magassag)
        

def modell_magassag(magassag):
    if magassag >= 170 and magassag <= 175:
        return "Kiváló, a modell alkalmazható"
    else:
        return "Elutasítva"

print(f"{nev} eredménye: {modell_kor(kor)}")
wr.write(f"{nev} eredménye: {modell_kor(kor)}")
wr.close()