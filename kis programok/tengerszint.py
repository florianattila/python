"""
def tengerszint(szint):
    if szint < 200:
        return True
    elif szint > 200 & szint < 500:
        return False

nev = "a"
while nev:
    nev = input("Add meg a földrajzi hely nevét!")
    if nev:
        szint = int(input("Add meg a tengerszint feletti magasságát"))
        if tengerszint:
            print(f"{nev} egy alföld")
        else:
            print(f"{nev} egy dombság")
"""

def tengerszint(szint):
    if szint < 200:
        return "alföld"
    elif szint < 500 and szint >= 200:
        return "dombság"
    elif szint >= 500 and szint <1500:
        return "középhegység"
    else:
        return "magashegység"

nev = "a"
while nev:
    nev = input("Add meg a földrajzi hely nevét!")
    if nev:
        szint = int(input("Add meg a tengerszint feletti magasságát"))
        print(f"{nev} egy {tengerszint(szint)}")