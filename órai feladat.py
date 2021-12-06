#1
a= input("adjon meg egy szót! ")
print(len(a))
#2
b= input("adjon meg egy szót! ")
print(b[0])
#3
c= input("adjon meg egy szót! ")
print(c[-1])
#4
d = input("Adjon meg egy 5 betűs szót")
print(d[1:4])
#5
iranyitoszam =input("adjon meg egy Budapesti irányitószámot! ")
if iranyitoszam[1:3] == "01":
    print("1. kerület")
elif iranyitoszam[1:3] == "02":
    print("2. kerület")
elif iranyitoszam[1:3] == "03":
    print("3. kerület")
elif iranyitoszam[1:3] == "04":
    print("4. kerület")
elif iranyitoszam[1:3] == "05":
    print("5. kerület")
elif iranyitoszam[1:3] == "06":
    print("6. kerület")
elif iranyitoszam[1:3] == "07":
    print("7. kerület")
elif iranyitoszam[1:3] == "08":
    print("8. kerület")
elif iranyitoszam[1:3] == "09":
    print("9. kerület")
elif iranyitoszam[1:3] == "10":
    print("10. kerület")
elif iranyitoszam[1:3] == "11":
    print("11. kerület")
elif iranyitoszam[1:3] == "12":
    print("12. kerület")
elif iranyitoszam[1:3] == "13":
    print("13. kerület")
elif iranyitoszam[1:3] == "14":
    print("14. kerület")
elif iranyitoszam[1:3] == "15":
    print("15. kerület")
elif iranyitoszam[1:3] == "16":
    print("16. kerület")
elif iranyitoszam[1:3] == "17":
    print("17. kerület")
elif iranyitoszam[1:3] == "18":
    print("18. kerület")
elif iranyitoszam[1:3] == "19":
    print("19. kerület")
elif iranyitoszam[1:3] == "20":
    print("20. kerület")
else: 
    print("Nem budapesti")
#6a
régi= "leszel"
régi = list(régi)
régi[0] = "L"
régi = "".join(régi)
print(régi)
#6b
régi= "leszel"
régi = list(régi)
régi[-1] = "k"
régi = "".join(régi)
print(régi)
#6c
régi= "leszel"
régi = list(régi)
régi[0] = ""
régi[-1] = ""
régi = "".join(régi)
print(régi)
#6d
régi = régi + "m"
#7
vezetek= input("Kérem a vezeték neved")
utó= input("Kérem a utóneved")
karakter = vezetek[0]
eredmeny = karakter + utó
print(eredmeny.lower())
#8
"""vezetek= input("Kérem a vezeték neved")
utó= input("Kérem a utóneved")"""
eredmeny = vezetek[0:3] + utó[0:3] + "01"
print(eredmeny.lower())
#9
szó = input("Adj meg egy szót")
if szó[0] == "e":
    print("e-vel kezdődik")
else:
    print("Nem e-vel kezdődik")
#10
szó1 = input("Adj meg egy szót")
szó2 = input("Adj meg egy szót")
if len(szó1) > len(szó2):
    print(szó1, szó2)
elif len(szó1) < len(szó2):
    print(szó2, szó1)
else:
    print("Ugyanolyan hosszúak")
#11
otbetu1 = input("Adjon meg egy 5 betűs szót")
otbetu2 = input("Adjon meg egy 5 betűs szót")
otbetu3 = otbetu1[1:4]
otbetu4 = otbetu2[1:4]
lista = []
lista.append(otbetu3)
lista.append(otbetu4)
lista.sort()
print(lista[0])