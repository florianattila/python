tippek = [3, 12, 1, 8, 5, 8, 1, 2, 1, 4]
tippek.index(2)+1
masolat = tippek.copy()
del tippek[3:5]
tippek.sort()
print(tippek)
tippek.reverse()
print(tippek)
hivatkozas = tippek
tippek.remove(12)
print(tippek)
print(hivatkozas)