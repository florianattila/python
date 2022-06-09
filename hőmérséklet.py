wr = open("hőmérséklet.txt","w")
hom= [9,-16,-19,-8,-2,14,15,16,-8,8,-3,-9,-4,-3,18,-17,-7,-1,7,10,-12,14,7,6,-6,-20,10,3]
def februar(hom):
    február = False
    if len(hom) == 28:
        február = True
        wr.write("Igen")
        return True
    else:
        wr.write("Nem")
        return február
print(februar(hom))

def minuszketto(hom):
    if -2 in hom:
        nap= hom.index(-2)+1
        wr.write(f"\nA {nap}. napon -2 fokos hőmérséklet volt")
        return f"A {nap}. napon -2 fokos hőmérséklet volt"
        
    else:
        wr.write("\nNem volt olyan nap")
        return "Nem volt olyan nap"
print(minuszketto(hom))

ossz = 0
legnagyobb = 0
legkisebb = 0
def hanyszor(hom, ossz, legkisebb, legnagyobb):
    hanyszor = 0
    for x in hom:
        ossz += x
        if x > legnagyobb:
            legnagyobb = x
        elif x < legkisebb:
            legkisebb = x
        if x  > -2:
            hanyszor += 1
    wr.write(f"\n{hanyszor} alkalommal volt -2°C alatti mérve")
    wr.write(f"\nA legnagyobb mért hőmérséklet {legnagyobb}°C")
    wr.write(f"\nA legkisebb mért hőmérséklet {legkisebb}°C")
    print(f"{hanyszor} alkalommal volt -2°C alatti mérve,\nA legkisebb mért hőmérséklet {legkisebb}°C, \nA legnagyobb mért hőmérséklet {legnagyobb}°C")
    return ossz, legnagyobb, legkisebb
hanyszor(hom, ossz, legkisebb, legnagyobb)
ossz = sum(hom)

legkisebb = min(hom)
legnagyob = max(hom)

def atlag(hom, ossz):
    átlag = ossz/len(hom)
    wr.write(f"\nAz átlagos hőmérséklet {átlag:.2f}°C volt")
    print(f"Az átlagos hőmérséklet {átlag:.2f}°C volt")
    return átlag
atlag(hom, ossz)

hoingadozas = 0
def hoingadozas(legnagyobb, legkisebb, hoingadozas):
    hoingadozas = legnagyobb-legkisebb
    wr.write(f"\nA hónapban a legnagyobb hőingadozás {hoingadozas}°C volt")
    print(f"A hónapban a legnagyobb hőingadozás: ",hoingadozas)
print(hoingadozas(legnagyobb,legkisebb, hoingadozas))

wr.close()