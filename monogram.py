wr = open("monogram.txt","w")
def monog(nev):
    szóköz = nev.index(" ")
    return nev[0]+"."+nev[szóköz+1] + "."
nev = input("Add meg a neved! ")
print(nev, "monogramja", monog(nev))
wr.write(f"{nev} monogramja {monog(nev)}")

def kisnagy(nev):
    return "nagybetűs: "+ nev.upper()+ "\nkisbetűs: " + nev.lower()
print(kisnagy(nev))
wr.write(f"{kisnagy(nev)}")