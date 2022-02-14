import random

zsak = [2,9,19,20,5,7.11]
#órai feladat
wr = open("zsák.txt","w")
össztömeg = sum(zsak)
wr.write(f"Az osztomeg {össztömeg}kg")
ötnél_nagyobb = 0
for i in zsak:
    if i > 5:
        ötnél_nagyobb += 1
wr.write(f'\n{ötnél_nagyobb}db 5-nel nagyobb zsak van')
darab = len(zsak)
átlag = össztömeg/darab
wr.write(f"\nA zsak atlaga {átlag}kg")
wr.write(f"\nA zsak {darab}db elemet tartalmaz")
minimum = min(zsak)
wr.write(f"\nA zsak legkisebb eleme {minimum}kg")
maximum = max(zsak)
wr.write(f"\nA zsak legnagyobb eleme {maximum}kg")

#Házifeladat

#A) Mennyi a 5 kg-nál nagyobb zsákok tömege?
nagyobb = 0
for x in zsak:
    if x >5:
        nagyobb += x
print(f"A 5kg-nal nagyobb zsakok ossztomege {nagyobb}kg")
wr.write(f"\nA 5kg-nal nagyobb zsakok ossztomege {nagyobb}kg")
#B) Egy molnár a hét napjain ezeket a zsákokat emelgette 
# (2 kg- hétfő és így tovább) Melyik napon emelt a legkevesebbet és melyiken a legtöbbet?
legkonyebb = min(zsak)
legnehezebb = max(zsak)
legkisebb_szama = zsak.index(legkonyebb)+1
legnagyobb_szama= zsak.index(legnehezebb)+1
print(f"A legkönyebb zsák {legkonyebb}kg volt, a {legkisebb_szama}. napon.")
wr.write(f"\nA legkönyebb zsák {legkonyebb}kg volt, a {legkisebb_szama}. napon.")
napok = zsak.index(legnehezebb)+1
print(f"A legnehezebb zsák {legnehezebb}kg volt, a {legnagyobb_szama}. napon")
wr.write(f"\nA legnehezebb zsák {legnehezebb}kg volt, a {legnagyobb_szama}. napon")

#C) A molnár a jövő heti lisztet is megrendelte. A kiszállítás nem egyenletes, így 5 és 50 kg között zsákokat fog kapni. Minden nap csak egyet. 
# Készítse el a kiszállítást szervező programot.
szam = 0
legnagyobb_csomag = 0
liszt = 0
while szam != 7:
    liszt = random.randint(5,50)
    if liszt > legnagyobb_csomag:
        legnagyobb_csomag = liszt
    szam += 1
    print(f"A(z) {szam}. napon {liszt}kg lisztet kapott")
    wr.write(f"\nA(z) {szam}. napon {liszt}kg lisztet kapott")
print(f"A legnehezebb {legnagyobb_csomag}kg volt")
wr.write(f"\nA legnehezebb {legnagyobb_csomag}kg volt")
wr.close()
"""
wr = open("zsák.txt","r")
print(wr.read())
"""