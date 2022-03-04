import random

egyenleg = 0
jelszo = 1212

def jelszo_ellenorzes(jelszo, proba, egyenleg):
    while proba > 0:
        key = int(input("Adja meg a pin kódot "))
        if key == jelszo:
            bank(egyenleg)
            break
        else:
            proba-=1
            if proba == 0:
                return "Hitelesítés megtagadva!\n -----------------------"
            else:
                return f"Helytelenül adta meg a pint, még {proba} próbálkozása maradt"
            
def felvetel(egyenleg):
        key = int(input(" 1: 1.000.000 \n 2: 500.000 \n 3: 250.000 \n 4: 100.000 \n 5: 50.000 \n 6: 10.000 \n 7: Más összeg \n"))
        if key == 1:
            felvetel=1000000
            if egyenleg - felvetel < 0:
                print("Nincsen elég egyenleg a számlán\n -----------------------")
                return bank(egyenleg)
            else:
                egyenleg -= felvetel;
                print("Felvette a pénzt\n -----------------------")
                return egyenleg, bank(egyenleg)
        elif key == 2:
            felvetel=500000
            if egyenleg - felvetel < 0:
                print("Nincsen elég egyenleg a számlán\n -----------------------")
                return bank(egyenleg)
            else:
                egyenleg -= felvetel;
                print("Felvette a pénzt\n -----------------------")
                return egyenleg, bank(egyenleg)
        elif key == 3:
                felvetel=25000;
                if egyenleg - felvetel < 0:
                    print("Nincsen elég egyenleg a számlán\n -----------------------")
                    return bank(egyenleg)
                elif egyenleg - felvetel >= 0:
                    egyenleg -= felvetel
                    print("Felvette a pénzt\n -----------------------")
                    return egyenleg, bank(egyenleg)
        elif key == 4:
                felvetel=100000
                if egyenleg - felvetel < 0:
                    print("Nincsen elég egyenleg a számlán\n -----------------------")
                    return bank(egyenleg)
                elif egyenleg - felvetel >= 0:
                    egyenleg -= felvetel
                    print("Felvette a pénzt\n -----------------------")
                    return egyenleg, bank(egyenleg)
        elif key == 5:
                felvetel=50000;
                if egyenleg - felvetel < 0:
                    print("Nincsen elég egyenleg a számlán\n -----------------------")
                    return bank(egyenleg)
                elif egyenleg - felvetel >= 0:
                    egyenleg -= felvetel
                    print("Felvette a pénzt\n -----------------------")
                    return egyenleg, bank(egyenleg)
        elif key == 6:
                felvetel=10000;
                if egyenleg - felvetel < 0:
                    print("Nincsen elég egyenleg a számlán\n -----------------------")
                    return bank(egyenleg)
                elif egyenleg - felvetel >= 0:
                    egyenleg -= felvetel
                    print("Felvette a pénzt\n -----------------------")
                    return egyenleg, bank(egyenleg)
        elif key == 7:
                felvetel = int(input("Adja meg az összeget! "))
                while felvetel % 1000 != 0:
                    felvetel = int(input("Ezerrel osztható számot adjon meg! "))
                    if egyenleg - felvetel < 0:
                        print("Nincsen elég egyenleg a számlán\n -----------------------")
                        return bank(egyenleg)
                    elif egyenleg - felvetel >= 0:
                        egyenleg -= felvetel
                        print("Felvette a pénzt\n -----------------------")
                        return egyenleg, bank(egyenleg)

def befizetes(egyenleg):
    befizet = int(input("Mennyit szeretne befizetni? "))
    egyenleg += befizet
    return "Sikeres befizetés", egyenleg, bank(egyenleg)

def bank(egyenleg):
    key = int(input("\n 1: Felvétel \n 2: Befizetés \n 3: Egyenleg \n 4: Kilépés \n"))
    if key == 1:
        felvetel(egyenleg)
    elif key == 2:
        befizetes(egyenleg)
    elif key ==3:
        print(f"-----------------------\nAz egyenlege: {egyenleg}ft\n-----------------------")
        bank(egyenleg)
    elif key == 4:
        print("Köszönjük hogy a mi bankunkat választotta!")
        lobby(egyenleg)

def lobby(egyenleg):
    key = int(input(" 1: Bank \n 2: Szerencsejáték \n 3: Kilépés"))
    if key == 1:
        jelszo_ellenorzes(jelszo,3, egyenleg)
    elif key == 2:
        casino(egyenleg)
    elif key == 3:
        return exit()
    else:
        return lobby(egyenleg)

def casino(egyenleg):
    key = int(input("-------------\nVálassz játékot! \n 1: Ötös löttó 300Ft(1,4 milliárd Ft) \n 2: Dobókocka (árx3) \n 3: Kilépés \n "))
    print(egyenleg)
    if key == 1:
        return lotto(egyenleg)
    elif key == 2:
        return dobokocka(egyenleg)
    elif key == 3:
        return lobby(egyenleg)

def dobokocka(egyenleg):
    print("-------------")
    tet = int(input("Adja meg a tétet "))
    tipp = int(input("Írj be egy tippet!"))
    egyenleg -= tet
    nyeroszam = random.randint(1,6)
    print(f"A nyerőszám: {nyeroszam}")
    if nyeroszam == tipp:
        print("Nyertél")
        egyenleg = egyenleg+(tet*3)
        return egyenleg, casino(egyenleg)
    else:
        print("Nem nyert :(")
        casino(egyenleg)
        
def lotto(egyenleg):
    tippek = []
    helyes = 0
    for _ in range(5):
        tipp = int(input("Adja meg az 1. tippet"))
        tippek.append(tipp)
    for _ in range(5):
        nyeroszam = random.randint(1,90)
        nyeroszamok = []
        nyeroszamok.append(nyeroszam)
    for nyeroszam in nyeroszamok:
        for tipp in tippek:
            if tipp == nyeroszam:
                helyes += 1
    if helyes == 5:
        nyeremeny = 1400000000
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
    elif helyes == 4:
        nyeremeny = 0
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
    elif helyes == 3:
        nyeremeny = 0
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
    elif helyes == 2:
        nyeremeny = 0
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
    elif helyes == 1:
        nyeremeny = 0
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
    elif helyes == 0:
        print("Nem volt helyes tipp")
 
lobby(egyenleg)