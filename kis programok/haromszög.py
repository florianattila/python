import math

a = int(input("Add meg az a oldalt"))
b = int(input("Add meg az b oldalt"))
c = int(input("Add meg az c oldalt"))
s = (a+b+c)/2
elsoszog = math.sqrt(s*(s-a)+(s-b)+(s-c))

a1 = int(input("Add meg az a oldalt"))
b1 = int(input("Add meg az b oldalt"))
c1 = int(input("Add meg az c oldalt"))
s1 = (a1+b1+c1)/2
masodikszog = math.sqrt(s1*(s1-a1)+(s1-b1)+(s1-c1))

if elsoszog > masodikszog:
    print("Az első szög nagyobb")
elif elsoszog < masodikszog:
    print("Második nagyobb")
else:
    print("Egyenlő")

