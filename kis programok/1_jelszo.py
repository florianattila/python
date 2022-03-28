import random
import math

#1.
def bejelentkezes():
    bejutott = False
    while not bejutott:
        user = input("Kérem adja meg a felhasználónevét!")
        jelszo  = input("Kérem adja meg a jelszavát!")
        if user == "teknos99" and jelszo == "Tokmag<3":
            print("Siker")
            bejutott = True
        else:
            print("Megtagadva te scammer")

#2.
def nevelo():
    maganhangzok= "aeáéiíoóöőuúüű"
    for _ in range(3):
        szo = input("Adjon meg egy főnevet")
        if szo[0].lower() in maganhangzok:
            print("A szó magánhangzóval kezdődik")
            print(f"Az {szo.upper()} {jelzo()}")
        else:
            print("A szó mássalhangzóval kezdődik")
            print(f"A {szo.upper()} {jelzo()} ")

def jelzo():
    return random.choice(["piros", "nagy", "könnyed", "buta"])

nevelo()

#3.
class Henger:
    def __init__(self, sugar, kozeppont = (0,0), magassag = 10):
        self.sugar = sugar
        self.kozeppont = kozeppont
        self.magassag = magassag
        def terulet(self):
            return self.sugar*math.pow(math.pi,2)
        def felszin():
            pass
        def terfogat():
            pass

hangszer = Henger(5,(2,4),12)