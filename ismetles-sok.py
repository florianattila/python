import random, io, codecs

szam1 = random.randint(10, 50)
szam2 = int(input("Adj meg egy számot"))
SZAM3 = 5
print(szam1, szam2, SZAM3)
if SZAM3%2 == 0:
    print("paros")
else:
    print("paratlan")

wr = open("kaprademon.txt", "w")
wr.write("kaprademon")
wr.close
"""""
wr = open("kaprademon.txt", "a",default_encoding=":utf-8")
wr.write("Szeretem a pytont")
print(wr)
wr.close
"""""
f = open("kaprademon.txt")
tartalom = f.read()
print(tartalom)
f.close()

lista2=[8, 10, 20]
with open("kaprademon.txt","w") as file :
    for item in lista2:
        file.write("%s\n"% item)

y = open ("M:\\JanzsóG\\10B_2021\\adat.txt","r")
tartalom = y.read()
print(tartalom)
y.close()