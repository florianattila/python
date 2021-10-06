"""
for i in range(1,101):
    print(i)

for i in range(1,101,2):
    print(i)

for i in range(1,101,-2):
    print(i)
"""
#prímszámok
for i in range(2, 101,):
    for oszto in range(2,i//2+1): #elkerüli hogy a 4 prímszám legyen
        if (i%oszto) == 0:
            break
    else:
        print(i , "prím")