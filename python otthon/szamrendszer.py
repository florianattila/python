def beker():
    atvaltas = int(input("Milyen számrendszerbe szeretnél átváltani? \n 1: kettes (bináris) \n 2: tizenhatos (hexadecimális) \n 3: tízes \n"))
    if atvaltas == 1:
        szam = int(input("Adj meg egy számot 0 és 2047 közt!"))
        while szam > 2047:
            print("A szám maximum 2047 lehet!")
            szam = int(input("Adj meg egy számot 0 és 2047 közt!"))
        binaris(szam)
    elif atvaltas == 2:
        szam = int(input("Adj meg egy számot 0 és 65535 közt!"))
        while szam > 65535:
            print("A szám maximum 65535 lehet!")
            szam = int(input("Adj meg egy számot 0 és 65535 közt!"))
        hexadecimalis(szam)
    elif atvaltas == 3:
        szamrendszer = int(input("Melyik számrendszerből? (2 vagy 16)"))
        if szamrendszer == 2:
            kettesbol()
        elif szamrendszer == 16:
            pass
        else:
            print("Ilyen nincs!")
    else:
        print("Nem jó")

def binaris(szam):
    binarisszam = ""
    eredeti = szam
    if szam-1024 >= 0:
        binarisszam += "1"
        szam -= 1024
    else:
        binarisszam += "0"
    if szam-512 >= 0:
        binarisszam += "1"
        szam -= 512
    else:
        binarisszam += "0"
    if szam-256 >= 0:
        binarisszam += "1"
        szam -=256
    else:
        binarisszam += "0"
    if szam-128 >= 0:
        binarisszam += "1"
        szam -=128
    else:
        binarisszam += "0"
    if szam-64 >= 0:
        binarisszam += "1"
        szam -=64
    else:
        binarisszam += "0"
    if szam-32 >= 0:
        binarisszam += "1"
        szam -=32
    else:
        binarisszam += "0"
    if szam-16 >= 0:
        binarisszam += "1"
        szam -=16
    else:
        binarisszam += "0"
    if szam-8 >= 0:
        binarisszam += "1"
        szam -=8
    else:
        binarisszam += "0"
    if szam-4 >= 0:
        binarisszam += "1"
        szam -=4
    else:
        binarisszam += "0"
    if szam-2 >= 0:
        binarisszam += "1"
        szam -=2
    else:
        binarisszam += "0"
    if szam-1 >= 0:
        binarisszam += "1"
        szam -=1
    else:
        binarisszam += "0"
    """
    while binarisszam[0] != "1":
        binarisszam[0] = ""
    """
    print(f"A(z) {eredeti} bináris alakja: {binarisszam}")

def hexaszamok(hexaszam, x):
    if x <= 9:
        hexaszam += str(x)
    elif x == 10:
        hexaszam += "A"
    elif x == 11:
        hexaszam += "B"
    elif x == 12:
        hexaszam += "C"
    elif x == 13:
        hexaszam += "D"
    elif x == 14:
        hexaszam = "E"
    elif x == 15:
        hexaszam += "F"
    return hexaszam
        
def hexadecimalis(szam):
    hexaszam = ""
    eredeti = szam
    x = 0

    # 16**3
    if szam-(16**3) > 0:
        x = szam//(16**3)
        hexaszam = hexaszamok(hexaszam, x)
        szam -= x*(16**3)
    else:
        hexaszam += "0"
    
    # 16**2
    if szam-(16**2) > 0:
        x = szam//(16**2)
        hexaszam = hexaszamok(hexaszam, x)
        szam -= x*(16**2)
    else: 
        hexaszam += "0"

    # 16
    if szam-16 > 0:
        x = szam//16
        hexaszam = hexaszamok(hexaszam, x)
        szam -= x*16
    else:
        hexaszam += "0"

    # 1
    if szam-1 > 0:
        x = szam//1
        hexaszam = hexaszamok(hexaszam, x)
        szam -= x*1
    else:
        hexaszam += 0

    print(f"A(z) {eredeti} hexadecimális alakja: {hexaszam}")

#Tízesbe
def kettesbol():
    igaze = False
    szam = input("Add meg a bináris számot! ")
    while igaze == False:
        for _ in range(10):
            for x in szam:
                if x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9":
                    szam = input("Ez nem bináris szám. Mást adj meg! ")
            igaze = True
    eredmeny = 0
    szamlista = []
    for c in szam: 
        c = int(c)
        szamlista.append(c)
    for y in reversed(szamlista):
        x = szamlista.index(y)
        eredmeny = eredmeny + y*(2**x)
    print(f"A {szam} tízes számrendszebeli alakja: {eredmeny}")


beker()