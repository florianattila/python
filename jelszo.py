#JELSZO = input("Mi a jelszava?")
JELSZO = "kiflisaroknyalogató"
jelszo = None
while jelszo != JELSZO:
    jelszo = input("Mi a jelszava?")
    if jelszo != JELSZO:
        print("Hibás jelszó")
print("Helyes jelszó")