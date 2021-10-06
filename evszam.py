evszam = int(input("Írja be a dátumot"))
if evszam%4 == 0 and evszam%100 != 0:
    print("Szökőév")
else:
    print("Nem szökőév")