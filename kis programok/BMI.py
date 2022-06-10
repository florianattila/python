nev = input("Adja meg a nevét! ")
magassag = int(input("Adja meg a magasságát cm-ben! "))
suly = int(input("Adja meg a testtömegét! "))
suly2 = suly/100
magassag2 = magassag**2
bmi = suly2/magassag2

if bmi <=16 :
    print("Ön súlyosan alultáplált")
elif bmi <=18.5:
    print("Ön alultáplált")
elif bmi <=25:
    print("Ön egészséges")
elif bmi <=30:
    print("Ön túlsúlyos")
else:
    print("érvényes adatok megadását kérem")