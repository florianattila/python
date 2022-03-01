auto_tipus = input("Adja meg az autó típusát")
gyartasi_ev = int(input("Adja meg a gyártási évet"))
sebesseg = int(input("Adja meg a sebességet"))

def auto_tipusok(auto_tipus):
    if auto_tipus[0] == "A" or auto_tipus[0] == "B":
        return "Német autó"
    else:
        return "Ismeretlen"

def gyartasi_ido(gyartasi_ev):
    if gyartasi_ev >= 2001 and gyartasi_ev != 2022:
        return "XXI. század"
    elif gyartasi_ev <= 2000:
        return "XX. század"
    elif gyartasi_ev == 2022:
        return "Mostani"

print(f"{gyartasi_ido(gyartasi_ev)}, {auto_tipusok(auto_tipus)}")