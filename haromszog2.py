wr = open("haromszog.txt","w")
haromszog = []
for x in range(3):
    oldal = int(input("Mekkora a háromszög oldalai"))
    haromszog.append(oldal)
print(f"A háromszög oldalai {haromszog}cm hosszuak")
wr.write(f"A háromszög oldalai {haromszog}cm hosszuak")
"""
legnagyobb = 0
legkisebb = 1000
for i in haromszog:
    if i > legnagyobb:
        legnagyobb = i
    elif i < legkisebb:
        i = legkisebb
"""
legkisebb = min(haromszog)
legnagyobb = max(haromszog)
print(f"A legnagyobb oldal {legnagyobb}cm, míg a legkisebb {legkisebb}cm")
wr.write(f"A legnagyobb oldal {legnagyobb}cm, míg a legkisebb {legkisebb}cm")
oldal_kereses = int(input("Mekkora oldalt keresel?"))
talalat = False
if oldal_kereses in haromszog:
    talalat = True
if talalat:
    print(f"Van {oldal_kereses}cm hosszú oldal")
    wr.write(f"Van {oldal_kereses}cm hosszú oldal")
else:
    print(f"Nincs {oldal_kereses}cm hosszú oldal")
    wr.write(f"Nincs {oldal_kereses}cm hosszú oldal")
wr.close()