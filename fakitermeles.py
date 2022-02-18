import random

wr = open("fa.txt", "w")
fa = []
szam = 0
while szam != 31:
    kitermeles = random.randint(50,100)
    fa.append(kitermeles)
    szam += 1

össz = 0
for megtermelt in fa:
    össz += megtermelt
print(f"A márciusi összes fatermelés {össz}")
wr.write(f"A marciusi osszes fatermeles {össz}m3")
"""
össz = sum(fa)
"""

átlag = össz/ len(fa)
print(f"A márciusi kitermelt fa átlaga: {átlag}")
wr.write(f"\nA marciusi kitermelt fa atlaga: {átlag}")
legkisebb = min(fa)
legnagyobb = max(fa)
"""
for i in fa:
    if i < legkisebb:
        legkisebb = i
    elif i > legnagyobb:
        legnagyobb = i
"""
print(f"a legkisebb {legkisebb} volt, a legnagyobb {legnagyobb}")
wr.write("\na legkisebb {legkisebb} volt, a legnagyobb {legnagyobb}")

"""
if 40 in fa:
    print("Volt olyan nap, ahol 40 volt a kitermelt fa")
    wr.write("\nVolt olyan nap, ahol 40 volt a kitermelt fa")
else:
    print("Nem volt olyan nap, amikor 40 volt a kitermelt fa")
    wr.write("\nNem volt olyan nap, ahol 40 volt a kitermelt fa")
"""

van40= False
for x in fa:
    if x == 40:
        print("Van ilyen")
        van40= True
        break
    else:
        print("Nincs ilyen")

#70 felett nagy termeles
nagy_termeles_szama = 0
nagy_termeles_összege = 0
for x in fa:
    if x > 70:
        nagy_termeles_szama += 1
        nagy_termeles_összege += x
print(f"{nagy_termeles_szama} alkalommal volt 70 feletti a napi termeles")
print(f"A 70 feletti termelések összege {nagy_termeles_összege}")
wr.write("f{nagy_termeles} alkalommal volt 70 feletti a napi termeles")
wr.write(f"A 70 feletti termelések összege {nagy_termeles_összege}")

össztermeles_szazaleka = nagy_termeles_összege/össz*100
print(f"Az össztermelesnek {össztermeles_szazaleka}%-a nagytermeles")
wr.write(f"Az össztermelesnek {össztermeles_szazaleka}%-a nagytermeles")

nagy_termeles_szazaleka = nagy_termeles_szama/len(fa)*100
print(f"A napok {nagy_termeles_szazaleka}%-ában nagy termeles volt")
wr.write(f"A napok {nagy_termeles_szazaleka}%-ában nagy termeles volt")
wr.close()