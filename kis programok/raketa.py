visszaszamlalas = int(input("Mennyitől számoljon vissza?"))
eltelt = visszaszamlalas
felfüggesztes = None
while visszaszamlalas != 0:
    felfüggesztes = input("Felfüggeszted? i/n")
    if felfüggesztes == "i" or felfüggesztes== "igen":
        print("A visszaszamlálást felfüggesztetted. ")
        eltelt += 1
    elif felfüggesztes == "n" or felfüggesztes == "nem":
        visszaszamlalas -=1
        print("A visszaszámlálás folytatódik. ")
        print(f"Még {visszaszamlalas}óra van a kilövésig")
print("A rakéta kilőtt")
print(f"{eltelt}óra telt el.")