import math
a = (input("Fő együttható:"))
a= float(a)
while a == 0:
    print("Ez nem lesz másodfokú, nem oldom meg")
    a = input("Fő együttható:")
    a = float(a)
b= input("Elsőfokú tag együttható")
c= input("Konstans tag:")
b = float(b)
c= float(c) 
d= b*b-4*a*c
if d >= 0:
    print ("van valós megoldás") 
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás" , x1)
    print("Az másik megoldás" , x2)
else:
    print("Nincs valós megoldás")
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print("Az egyik megoldás" , x1)
    print("Az másik megoldás" , x2)