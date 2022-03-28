import math
import random

#kör
class Kor:
    def __init__(self, r, kozeppont=(0,0)): #KONSTRUKTOR
        self.r = r
        self.kozeppont = kozeppont
    def terulet(self):
        return self.r*self.r*math.pi
    def kerulet(self):
        return 2*self.r*math.pi
    def info(self):
        print(f"A(z) {self.r}cm sugarú {self.kozeppont} középpontű körnek \n telülete {self.terulet():.2f}cm\n kerülete: {self.kerulet():.2f}cm")

#példány
kor01 = Kor(5,(2,6))
kor01.info()
print(isinstance(kor01,Kor)) #Azonos típus? -> True / False
print(type(kor01))

#metodus
print(f"{kor01.terulet():.2f}")

korok = []

for _ in range(5):
    kor = Kor(random.randint(0,10))
    korok.append(kor)

for x in korok:
    x.info()