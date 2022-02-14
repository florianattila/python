EPER = "eper"
CSOKI = "csoki"
VANILLIA = "vanillia"
CSOKISKEKSZ = "csokiskeksz"
fagyi=None
print("Választék: eper, csoki, vanilla, csokiskeksz, karamell")
while fagyi != EPER or fagyi != CSOKI or fagyi != VANILLIA or fagyi != CSOKISKEKSZ or fagyi != "karamell":
    fagyi = input("Milyen fagyit kérsz?")
    print("Ilyen fagyink nincs")
gombóc = int(input("Hány gombócot kérsz?"))
tölcsér = input("Milyen tölcsért kérsz?")
if tölcsér != "sima":
    print("Csak sima van, azt kapsz")
else:
    print("Jó választás")
ár = (gombóc*330)
print('Jó étvágyat a',  gombóc , "gombóc" , fagyi , "fagyihoz" , ár , "ft lesz!")