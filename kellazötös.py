pont = 0
tipus = input("Milyen tipusa van a gépnek?")
if tipus == "ZX spectrum" or tipus == "C64":
    pont += 1
else:
    print("nem jó a típus")

mukodik = input("Működik?")
if mukodik == "igen":
    pont += 1
else:
    print("Nem kell ha nem működik")

ar = int(input("mennyibe kerül?"))
if ar <= 25000:
    pont += 1
else:
    print("Túl sok")

if pont == 3:
    print("Megfelelő a gép")