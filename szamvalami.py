import random

szam = random.randint(10,50)
szam2 = random.randrange(10,50)
lista= [szam, szam2]
lista2= []
if szam > szam2:
    a = szam/szam2
    b = szam//szam2
    c = szam%szam2
else:
    a = szam2/szam
    b = szam2//szam
    c = szam2%szam

for i in lista:
    print(i)
print("for ciklus")

lista2.append(a)
lista2.append(b)
lista2.append(c)
lista2.sort()
print(lista2)