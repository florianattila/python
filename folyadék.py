össz = 0
while össz <= 35 and (ivás:=int(input("Hány decit ittál?"))):
    print(f"Már {(össz:=össz+ivás)/10:3.1} litert ittál")
    if össz >= 25:
        print("Már ikerült elérned a 2,5litert")
print("Béka nő a hasadban")