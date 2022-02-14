import random

zsak = [2,9,19,20,5,7.11]
# A) Mennyi a 5 kg-nál nagyobb zsákok tömege?
nagy_zsakok = 0
for x in zsak:
    if x > 5:
        nagy_zsakok += 1
print(f"{nagy_zsakok}db 5kg-nál nagyobb zsák van.")

#B) Egy molnár a hét napjain ezeket a zsákokat emelgette (2 kg- hétfő és agy tovább) Melyik napon emelt a legkevesebbet és melyiken a legtöbbet?
legkisebb = min(zsak)
legnagyobb = max(zsak)
legkisebb_szama = zsak.index(legkisebb)+1
legnagyobb_szama= zsak.index(legnagyobb)+1
print(f"A legkönnyebb napja a {legkisebb_szama}. nap lesz, {legkisebb}kg-mal")
print(f"A legnehezebb napja a {legnagyobb_szama}. nap lesz, {legnagyobb}kg-mal")

#C) A molnár a jövő heti lisztet is megrendelte. A kiszállítás nem egyenletes, így 5 és 50 kg között zsákokat fog kapni. Minden nap csak egyet. Készítse el a kiszállítást szervező programot.
szam = 0
legnagyobb_csomag = 0
liszt = 0
while szam != 7:
    liszt = random.randint(5,50)
    if liszt > legnagyobb_csomag:
        legnagyobb_csomag = liszt
#D) mondja meg a molnárnak melyik lesz a "legnehezebb" napja!.
print(f"A legnagyobb csomag {legnagyobb}kg volt")
#E) Hozzon létre egy zsakhf nevű állományt és az A-D feladatok eredményét írassa!
wr = open("zsakhf.txt","w")
wr.write(f"{nagy_zsakok}db 5kg-nal nagyobb zsak van.")
wr.write(f"\nA legkonnyebb napja a {legkisebb_szama}. nap lesz, {legkisebb}kg-mal \nA legnehezebb napja a {legnagyobb_szama}. nap lesz, {legnagyobb}kg-mal")
wr.write(f"\nA legnagyobb csomag {legnagyobb_csomag}kg volt")
wr.close()