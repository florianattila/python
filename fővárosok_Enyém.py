import random
from random import seed
from random import sample
seed(1)
sequence = [i for i in range(20)]
print(sequence)
subset = sample(sequence, 1)
print(subset)

fovarosok = []
fovarosok = ["Bécs", "Bern", "Párizs", "London", "Budapest", "Varsó", "Prága", "Róma", "Madrid", "Helsinki","Moszkva","Zágráb"]
fváros = None
while fváros !='':
    print('fvárosk jelenleg:' , ', '.join(fovarosok))
    fváros = input('Kérek egy fvárost!')
    if fváros != '':
        fovarosok.append(fváros)
#n = random.randint(

for index, főváros in enumerate(fovarosok):
    print(index, főváros)
    
#n = int(subset)
#print('A számítógép szerint ez a főváros a legszebb:', fovarosok[n])    

while len(fovarosok)> 0:
    print('fovárosaink:', ', '.join(fovarosok))
# A zárójelben átadott lista elemeit fűzi össze egyetlen karakterlánccá, az elemek közé pedig az elején, 
# aposztrófok között megadott karakterláncot teszi.
    melyik = input('Melyik főváros a legszebb, válaszd ki! ')
    if melyik in fovarosok:
        fovarosok.remove(melyik)
    else:
        print('Ilyen város nincs a listába')
        

print('Az első fváros: ', fovarosok[0])
print('A második fváros: ',fovarosok[1])
print('A harmadik fváros: ',fovarosok[1])
print('A sereghajtó/ utolsó fváros:', fovarosok[1]-1)