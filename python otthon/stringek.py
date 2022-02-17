szoveg = "Nagyon szeretem az vizet!"
print(szoveg)

#replace 
szoveg = szoveg.replace("vizet", "tejet").replace("az", "a") + "-És a kakaót is?"
print(szoveg)

#index
print(szoveg.index("tej"))
print(len(szoveg))
print(szoveg.startswith("Nagyon"))
print(szoveg.endswith("!"))
szoveg[-3:] #utolso 3 betu

szoveg2 = "                        Ma elmegyek futni.           "
print(szoveg2.lstrip) #left strip
print(szoveg2.rstrip) #right strip
print(szoveg2.strip) #midketto

#split
adatok = "0,1,2,3,4,5,6,7,8,9"
adatok = adatok.split(",")
print(adatok)

adatok2 = "Eni;Zsóka;Andi;Réka;Zsuzsi"
adatok2= adatok2.split(";")
print(adatok2)