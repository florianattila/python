wr = open("hőmérséklet.txt","w")
hom= [9,-16,-19,-8,-2,14,15,16,-8,8,-3,-9,-4,-3,18,-17,-7,-1,7,10,-12,14,7,6,-6,-20,10,3]
február = False
if len(hom) == 28:
    február = True
    print("Igen")
    wr.write("Igen")
else:
    print("Nem")
    wr.write("Nem")

nap = 0
if -2 in hom:
    nap= hom.index(-2)+1
    print(f"A {nap}. napon -2 fokos hőmérséklet volt")
    wr.write(f"\nA {nap}. napon -2 fokos hőmérséklet volt")
else:
    print("Nem volt olyan nap")
    wr.write("\nNem volt olyan nap")

legnagyobb = 0
legkisebb = 0
össz = 0
hanyszor = 0
for x in hom:
    össz += x
    if x > legnagyobb:
        legnagyobb = x
    elif x < legkisebb:
        legkisebb = x
    if x  > -2:
        hanyszor += 1
print(f"{hanyszor} alkalommal volt -2°C alatti mérve")
wr.write(f"\n{hanyszor} alkalommal volt -2°C alatti mérve")
print(f"A legnagyobb mért hőmérséklet {legnagyobb}°C")
wr.write(f"\nA legnagyobb mért hőmérséklet {legnagyobb}°C")
print(f"A legkisebb mért hőmérséklet {legkisebb}°C")
wr.write(f"\nA legkisebb mért hőmérséklet {legkisebb}°C")
"""
legkisebb = min(hom)
legnagyob = max(hom)
"""
átlag = össz/len(hom)
print(f"Az átlagos hőmérséklet {átlag:.2f}°C volt")
wr.write(f"\nAz átlagos hőmérséklet {átlag:.2f}°C volt")

hőingadozás = legnagyobb-legkisebb
print(f"A hónapban a legnagyobb hőingadozás {hőingadozás}°C volt")
wr.write(f"\nA hónapban a legnagyobb hőingadozás {hőingadozás}°C volt")
wr.close()