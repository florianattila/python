import random

hatosok = 0
dobasok_szama = int(input("Hányszor szeretnél dobni?"))
#Flórián Attila
while dobasok_szama != 0:
    dobasok_szama -=1
    dobas = random.randint(1,6)
    print(dobas)
    if dobas == 6:
        hatosok += 1

print(f'{hatosok} alkalommal dobtál 6-ot')
