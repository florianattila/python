mondat = ["Én", "elmentem", "a", "vásárba", "fél", "pénzzel."]
print("A mondat", len(mondat), "szóból áll")

legrövidebb_szó_hossza = 100000
for szó in mondat:
    if len(szó) < legrövidebb_szó_hossza:
        legrövidebb_szó_hossza = len(szó)
print(f"A legrövidebb szó hozza{legrövidebb_szó_hossza} betű")

írásjelek=".?!"
for szó in mondat:
    if szó[-1] in írásjelek:
        print("Van olyan szó aminek mondatvégi írásjel van a végén")

névelők = ["a", "az", "egy"]
for szó in mondat:
    if szó in névelők:
        print("Van a mondatban névelő")
        break

print(f"A mondatban a 'fél' szó a {mondat.index('fél')+1}. helyen áll")

van_nagy_kezdőbetűs = False
hol_van = None
for index in range(len(mondat)):
    if mondat[index][0].isupper():
        van_nagy_kezdőbetűs = True
        hol_van = index
    
if van_nagy_kezdőbetűs:
    print("A(z)", hol_van+1, ". szó kezdődik nagy betűvel")
