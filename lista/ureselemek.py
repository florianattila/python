#elemek
elemek= []
elemek.append(1)
elemek.append(2)
elemek.insert(2,3)
elemek.extend([4, 5, 6, 7, 8])
elemek.append(8)
print(elemek.count(8))
print(elemek)
print("Az elek lista 3. karakter:", elemek[2])
for elem in enumerate(elemek):
    print(elem)

#szavak
szavak=[]
szavak.append("barack")
szavak.append("ceruza")
szavak.append("alma")
szavak.append("diszkvalifikálás")
szavak.sort()
print(szavak)