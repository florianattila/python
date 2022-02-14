bevetelek = [3,8,10,19.35,-6,5.1,9,20]
vasarolte = False
for bevetel in bevetelek:
    if bevetel <0:
        vasarolte = True
        break
if vasarolte:
    print(f'vett valamit csesze meg')
else:
    print(f'A pincérnek fizettek')

n = len(bevetelek)
print(n)
print(f'bevétel{sum(bevetelek)}')
print(f'Átlag {sum(bevetelek)/n}' )



print({})
wr = open ('pincer.txt','w')
for i in bevetelek:
    wr.write(f'{i}\n')
wr.write(f'bevetel {str(sum(bevetelek))}')
wr.close()
ennyiszerkapfont = 0
for bevetel in bevetelek:
    if bevetel > 0 and bevetel % 1 !=0:
        ennyiszerkapfont += bevetel % 1
print(f'a pincér {ennyiszerkapfont*100} pennyt')