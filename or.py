def alahuzas ():
    for _ in range(10):
        print('-', end="")
    print("")
print("ez egy fontos sor")

def alahuzas (jel):
    for _ in range(10):
        print(jel, end="")
    print("")
print("ez egy fontos sor")
alahuzas("~")
print("ez egy fontos sor")
alahuzas("*")
print("ez egy fontos sor")
alahuzas("ˇ")

def pluszketto(szam):
    return szam+2

print("5+2 =", pluszketto(5))
pluszketto(5)
print("4+2 =", pluszketto(4))
pluszketto(4)

def megitel(mondat):
    if len(mondat) > 0:
        if mondat[-1] != "!" and mondat[-1] !="?" and mondat[-1] != ".":
            print(" >:-( ")
        else:
            print(" :-) ")

mondat = None
while mondat != "":
    mondat= input("Írj ide egy mondatot! ")
    megitel(mondat)

def pozneg(szam):
    if szam > 0:
        print(szam,"pozitív")
    elif szam < 0:
        print(szam, "negatív")
    elif szam == 0:
        print(szam, "nulla")
szam= None
while szam != "":
    szam= input("Írj egy számot")
    if szam != "":
        szam = float(szam)
        pozneg(szam)