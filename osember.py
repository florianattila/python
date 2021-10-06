nev = input("Adja meg a nevét!")
bogyo = int(input("Hány bogyója van?"))
if bogyo < 20:
    minosites = "ügyetlen"
elif bogyo > 20:
    minosites = "ügyes"
print(f'{nev} {minosites} minősítést kapott {bogyo}db bogyóval.')