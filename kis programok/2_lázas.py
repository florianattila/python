def laz(hom):
    if hom  >= 37:
        return "Lázas"
    else:
        return "Nem lázas"

for _ in range(3):
    nev = input("Adja meg a nevét")
    hom= float(input("Mekkora a testhőmérsékleted?"))
    print(f"{nev} állapota: {laz(hom)}")