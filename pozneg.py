szam = None
def pozneg(szam):
    if szam > 0:
        print(szam, 'pozitív.')
    elif szam < 0:
        print(szam, 'negatív.')
    else:
        print('A szám nulla.')

while szam != " ":
    szam = input("Adj szám!")
    if szam != " ":
        szam = float(szam)
    pozneg(szam)

wr=open("FA","w")
wr.write("FA")
wr.close()