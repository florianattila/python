nev = input("Mi legyen a file neve? ")
nev += ".txt"
wr = open(nev, "w")

wr.write(input("Írjon valamit a txt-jébe: "))


find_mondat = "Keress ebben a mondatban e betűket."
xy = find_mondat.find("e")
print(f"Ebben a mondatban {xy} e betű van!")


end = ("stop")
while end != ("stop"):
    print("Ha kész van írja be, hogy [stop]: ")
    if (end == "stop"):
        break

wr.close()