def beolvas():
    zenek = []                          # Ebben a listában fogjuk eltárolni a beolvasott zenéket

    with open("playlist.csv", "r", encoding="utf-8") as file:
        sorok = file.readlines()        # A fájl összes sorának beolvasása (a sorvége jeleket megtartja a sorok végén!)

        for sor in sorok:               # A beolvasott sorok bejárása
            sor = sor.strip()           # Eltávolítjuk a sorvége jeleket (itt az `rstrip()` függvényt is használhatnánk)
            darabok = sor.split(";")    # Feldaraboljuk a sort pontosvesszők mentén

            # A feldarabolás után eltároljuk a zene adatait egy dictionary-ben (a hossz egész szám, a többi adat string)
            zene = {"eloado": darabok[0], "cim": darabok[1], "mufaj": darabok[2], "hossz": int(darabok[3])}

            zenek.append(zene)          # Az elkészített dictionary-t beszúrjuk a zenéket tároló lista végére

    return zenek                        # A visszatérési érték a zenéket tároló lista


# === 2. feladat: Lejátszási lista teljes hossza ===

def teljes_hossz(zenek):
    hossz = 0

    for zene in zenek:                  # Összeadogatjuk a zenék hosszát egy `hossz` nevű változóban
        hossz += zene["hossz"]

    hossz_perc = hossz // 60            # Az így kapott hosszt átváltjuk percekbe és másodpercekbe
    hossz_masodperc = hossz % 60

    with open("02_hossz.txt", "w", encoding="utf-8") as file:   # Az eredményt kiírjuk a kimeneti fájlba
        file.write(f"A lejatszasi lista hossza: {hossz_perc} perc, {hossz_masodperc} masodperc\n")

# === főprogram ===
if _name_ == '_main_':
    lejatszasi_lista = beolvas()

    teljes_hossz(lejatszasi_lista)