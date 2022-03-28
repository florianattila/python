wr = open("2_vizsgazo.txt", "w")

def ellenoriz(nev,pont):
    if pont >= 48:
        atmegy = True
        print(f" {nev} eredménye: Átment")
        wr.write(f" {nev} eredménye: Átment")
    else:
        atmegy = True
        print(f"{nev} eredménye: Nem megy át")
        wr.write(f"{nev} eredménye: Nem megy át")
    return atmegy, beker()


def beker():
    nev = "a"
    while nev != "":
        nev=input("Adja meg a nevét")
        if nev:
            pont=int(input("Adja meg a pontszámot"))
            return ellenoriz(nev,pont)
    
beker()
