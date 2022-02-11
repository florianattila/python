lista = [ 3, 8, 2, 4, 5, 1, 6]
eredmeny = 0
for i in lista:
    if i > 5:
        eredmeny += 1
print(f'{eredmeny}db 5-nél nagyobb szám van a listában')