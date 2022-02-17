import math

class Szemely:
    def __init__(self,nev):
        self.nev = nev

sz1 = Szemely("Gábor")

def negyzet(x):
    return x*x

def gyok(x):
    return x**0.5

def muvelet(feladat, szam):
    return feladat(szam)

m1 = muvelet(negyzet, 10)
m2 = muvelet(math.sin, 5)
m3 = muvelet(math.cos, 4)
m4 = muvelet(lambda x: x*x*x, 10)
print(m1)
print(m2)
print(m3)