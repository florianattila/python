import random
kör = None
valasztas = ["kő", "papír", "olló"]
while kör != "nem":
    ellenfel = random.choice(valasztas)
    jatekos = input("kő, papír, olló")
    if jatekos == "kő":
        if ellenfel == "kő":
            print("döntetlen")
        elif ellenfel == "papír":
            print("vesztettél")
        else:
            print("nyertél")
    if jatekos == "papír":
        if ellenfel == "papír":
            print("döntetlen")
        elif ellenfel == "olló":
            print("vesztettél")
        else:
            print("nyertél")
    if jatekos == "olló":
        if ellenfel == "olló":
            print("döntetlen")
        elif ellenfel == "kő":
            print("vesztettél")
        else:
            print("nyertél")
    print("Az ellenfeled választása", ellenfel , "volt")
    print("------------")
    kör = input("Szeretnél még játszani? (igen/nem)")
print("Köszönöm a játékot!")