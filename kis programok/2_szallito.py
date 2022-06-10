def aru(suly):
    if suly >= 48:
        return True
    else:
        return False

nev = "abcdefghijklmnopqrstuvwxyz"
while nev:
    nev = input("Adja meg a termék nevét! ")
    if nev:
        suly = int(input("Adja meg a súlyát! "))
        if aru(suly):
            print(f"A {nev} mennyisége a raktárkészletben elegendő")
        else:
            print(f"A {nev} mennyisége a raktárkészletben NEM elegendő")
