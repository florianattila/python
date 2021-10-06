import math
a = input("fő együttható")
a = float(a)
while a == 0:
    print("Ez nem másodfokú")
    a = input("fő együttható")
    a = float(a)
b = input("Adja meg a másik együtthatót")
c = input("konstans tag")
b = float(b)
c = float(c)
d = b*b-4*a*c
print("A diszkrimináns: ", d )
if d >=0:
    print("Van valós megoldás")
    x1= (-b-math.sqrt(d))/(2*a)
    x2= (-b+math.sqrt(d))/(2*a)
    print("egyik megoldás:", x1)
    print("másik megoldás:", x2)
else:
    print("Nincs valós megoldás")
    x1= (-b-math.sqrt(d))/(2*a)
    x2= (-b+math.sqrt(d))/(2*a)
    print("egyik megoldás:", x1)
    print("másik megoldás:", x2)