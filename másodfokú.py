import math
a = input("Adja meg az első együtthatót")
a = float(a)
while a == 0: 
    print("Ez nem másodfokú, nem oldom meg!")
    a = input("Adja meg az első együtthatót")
    a = float(a)
b = input("Kérem az elsőfokú tag együtthatóját")
b = float(b)
c = input("Kérem a konstans tagot")
c = float(c)
d = b*b-4*a*c
print("diszkrimináns értéke", d)
if d >=0:
    print("Van valós megoldás")
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás:", x1)
    print("A másik megoldás:", x2)
else:
    print("Nincs valós megoldás")
    x1 = (-b-math.sqrt(d))/(2*a)
    x2 = (-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás:", x1)
    print("A másik megoldás:", x2)