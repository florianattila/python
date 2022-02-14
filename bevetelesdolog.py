bevetelek = [3,8,10,19.35,-6,5.1,9,20]
vendegek = 0
for bevetel in bevetelek:
    if bevetel > 0:
        vendegek += 1

print("A pincér", round(vendegek/2,2) ,"font fizetést kap.")