nev = input("Andja meg az ősember nevet!")
bogyo = int(input("Hány bogyója van?"))
if bogyo < 10:
    minosites = 'zsenge'
elif bogyo > 20:
    minosites = 'nagy koponya'
else:
    minosites = 'gyűjtögető'
print(f' {nev} egy {minosites}')