def beker():
    barack = int(input("Mennyi barack termett? "))
    kereskedo = int(input("Mennyit rendeltek a kereskedők? "))
    return barack,kereskedo

def megnez():
    if barack < kereskedo:
        print("Többet rendeltek")
    elif kereskedo < barack:
        print("Több termett")
    else:
        print("Pont ugyanannyit rendeltek mint amennyi termett")

barack, kereskedo = beker()
megnez()