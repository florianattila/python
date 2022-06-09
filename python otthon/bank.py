import random

#Pénz osztály
class Penz:
    def __init__(self, huf):
        self.huf = huf
        self.euro = huf/387
        self.font = huf/469
        self.dollar = huf/354
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return Penz(self.huf + other)
    def kiir(self, value):
        if value == "huf":
            return f"{self.huf:.0f}ft"
        elif value == "euro":
            return f"{self.euro:.2f}€"
        elif value == "font":
            return f"{self.font:.2f}£"
        elif value == "dollar":
            return f"{self.dollar:.2f}$"
egyenleg = 0
jelszo = 1212
egyenleg2 = Penz(egyenleg)

#Jelszo
def jelszo_ellenorzes(jelszo, proba, egyenleg):
    while proba > 0:
        key = int(input("Adja meg a pin kódot "))
        if key == jelszo:
            bank(egyenleg)
            break
        else:
            proba-=1
            if proba == 0:
                print("Hitelesítés megtagadva!\n -----------------------") 
            else:
                print(f"Helytelenül adta meg a pint, még {proba} próbálkozása maradt")

#Pénz felvétele            
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

#Befizetés
def befizetes(egyenleg):
    befizet = int(input("Mennyit szeretne befizetni? "))
    egyenleg += befizet
    return "Sikeres befizetés", egyenleg, bank(egyenleg)

#Bank belépés
def bank(egyenleg):
    key = int(input("\n 1: Felvétel \n 2: Befizetés \n 3: Egyenleg \n 4: Vissza \n"))
    if key == 1:
        felvetel(egyenleg)
    elif key == 2:
        befizetes(egyenleg)
    elif key ==3:
        egyenleg2 = Penz(egyenleg)
        print(f"-------------------\nAz egyenlege:\n {egyenleg2.kiir('huf')} \n {egyenleg2.kiir('euro')} \n {egyenleg2.kiir('font')} \n {egyenleg2.kiir('dollar')} \n-------------------")
        bank(egyenleg)
    elif key == 4:
        print("Köszönjük hogy a mi bankunkat választotta!")
        lobby(egyenleg)

#Lobby
def lobby(egyenleg):
    key = int(input(" 1: Bank \n 2: Szerencsejáték \n 3: Arcade \n 4: Kilépés \n"))
    if key == 1:
        jelszo_ellenorzes(jelszo,3, egyenleg)
    elif key == 2:
        casino(egyenleg)
    elif key == 3:
        arcade(egyenleg)
    elif key == 4:
        return exit()
    else:
        return lobby(egyenleg)

#Casino
def casino(egyenleg):
    key = int(input("-------------\nVálassz játékot! \n 1: Ötös lottó 300Ft(1,4 milliárd Ft) \n 2: Dobókocka (árx3) \n 3: Vissza \n "))
    if key == 1:
        return lotto(egyenleg)
    elif key == 2:
        return dobokocka(egyenleg)
    elif key == 3:
        return lobby(egyenleg)

#Dobókocka
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
<<<<<<< HEAD

#Lottó   
def lotto(egyenleg):
    egyenleg -= 300
    tippek = []
    helyes = 0
    nyeroszamok = []
    for _ in range(5):
        tipp = int(input("Adja meg a tippeket"))
        tippek.append(tipp)
    for _ in range(5):
        nyeroszam = random.randint(1,90)
=======
        
def lotto(egyenleg):
    tippek = []
    helyes = 0
    for _ in range(5):
        tipp = int(input("Adja meg az 1. tippet"))
        tippek.append(tipp)
    for _ in range(5):
        nyeroszam = random.randint(1,90)
        nyeroszamok = []
>>>>>>> a14f8a85954e57a2837951be7c070056b0fe25a3
        nyeroszamok.append(nyeroszam)
    for nyeroszam in nyeroszamok:
        for tipp in tippek:
            if tipp == nyeroszam:
                helyes += 1
    if helyes == 5:
        nyeremeny = 1400000000
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
<<<<<<< HEAD
        egyenleg += nyeremeny
    elif helyes == 4:
        nyeremeny = 10000000
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
        egyenleg += nyeremeny
    elif helyes == 3:
        nyeremeny = 500000
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
        egyenleg += nyeremeny
    elif helyes == 2:
        nyeremeny = 5000
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
        egyenleg += nyeremeny
    elif helyes == 1:
        nyeremeny = 300
        print(f"{helyes}db helyes tippet adott meg, nyereménye: {nyeremeny}")
        egyenleg += nyeremeny
    elif helyes == 0:
        print("Nem volt helyes tipp")
    return casino(egyenleg)

#Arcade
def arcade(egyenleg):
    print("---------------------")
    key = int(input("Válassz játékot!\n 1: Legyen ön is milliomos\n 2: Vissza"))
    if key == 1:
        legyenonis(egyenleg)
    elif key == 2:
        lobby(egyenleg)

# Legyen ön is millomos
class Kerdes:
    def __init__(self,kerdes, a, b, c, d, megoldas):
        self.kerdes = kerdes
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.megoldas = megoldas

#segitsegek_lista
def felezes(kerdes = Kerdes("kerdes", "a", "b", "c", "d", "megoldas")):
    torlesekA = ["B","C"],["B","D"],["C","D"]
    torlesekB = ["A","C"],["A","D"],["C","D"]
    torlesekC = ["A","B"],["A","D"],["B","D"]
    torlesekD = ["A","B"],["A","C"],["B","C"]
    if kerdes.megoldas == "A":
        torles = random.choice(torlesekA)
    elif kerdes.megoldas == "B":
        torles = random.choice(torlesekB)
    elif kerdes.megoldas == "C":
        torles = random.choice(torlesekC)
    elif kerdes.megoldas == "D":
        torles = random.choice(torlesekD)
    for torol in torles:
        if torol == "A":
            kerdes.a == "-"
        elif torol == "B":
            kerdes.b == "-"
        elif torol == "C":
            kerdes.c == "-"
        elif torol == "D":
            kerdes.d == "-"
    return kerdes

def kozonseg(kerdes = Kerdes("kerdes", "a", "b", "c", "d", "megoldas")):
    szam1 = random.randint(100)
    szam2 = random.randint(100)
    szam3 = random.randint(100)
    szam4 = random.randint(100)
    while szam1 + szam2 + szam3+ szam4 != 100 and szam1 > szam2 and szam1 > szam3 and szam1 > szam4:
        if kerdes.megoldas == "A":
            print(f"{kerdes.kerdes} \n A: {kerdes.a} {szam1} \n B: {kerdes.b} {szam2} \n C: {kerdes.c} {szam3} \n D: {kerdes.d} {szam4}\n ")
        elif kerdes.megoldas == "B":
            print(f"{kerdes.kerdes} \n A: {kerdes.a} {szam2} \n B: {kerdes.b} {szam1} \n C: {kerdes.c} {szam3} \n D: {kerdes.d} {szam4}\n ")
        elif kerdes.megoldas == "C":
            print(f"{kerdes.kerdes} \n A: {kerdes.a} {szam3} \n B: {kerdes.b} {szam2} \n C: {kerdes.c} {szam1} \n D: {kerdes.d} {szam4}\n ")
        elif kerdes.megoldas == "D":
            print(f"{kerdes.kerdes} \n A: {kerdes.a} {szam4} \n B: {kerdes.b} {szam2} \n C: {kerdes.c} {szam3} \n D: {kerdes.d} {szam1}\n ")
    return kerdes


def segitsegek(segitsegek_lista = [], kerdes = Kerdes("kerdes", "a", "b", "c", "d", "megoldas")):
    print("-------------")
    for x in segitsegek_lista:
        print(x)
    key = input("Milyen segítséget kérsz?")
    key = key.lower()
    while key not in segitsegek_lista or key == "":
        key = input("Nincs ilyen segítséged. Válassz mást!")
    if key == "felezés":
        segitsegek_lista.remove("felezés")
        felezes(kerdes)
    elif key == "közönség":
        segitsegek_lista.remove("közönség")
        kozonseg(kerdes)
    elif key == "":
        exit()
    return kerdes


#Könnyű
konnyu_kerdes1 = Kerdes("Mi Görögország fővárosa?", "Athén", "Bern","Olümposz", "Ankara", "A")
konnyu_kerdes2 = Kerdes("Mi a 'pityóka' szó jelentése?", "borsó", "pálinka", "krumpli", "részeg", "C")
konnyu_kerdes3 = Kerdes("Hogy hívják a hím kacsát?", "gácsér", "gúnár", "tojó", "kakas", "A")
konnyu_kerdes4 = Kerdes("Ki volt a Legyen ön is milliomos 1. műsorvezetője?", "Fábry Sándor", "Friderikusz Sándor", "Gundel Takács Gábor", "Vágó István", "D")
konnyu_kerdes5 = Kerdes("Melyik egy nemzetközi magyar étel neve?", "kondás", "kanász", "gulyás", "juhász", "C")
konnyu_kerdes6 = Kerdes("Milyen pitypangnak hívják a gyermekláncfüvet?", "pipogya", "patyolat", "pongyola", "papucs", "C")
konnyu_kerdes7 = Kerdes("Hova sorolhatóak a békák?", "hüllők", "puhatestűek", "kétéltűek", "emlős", "C")
konnyu_kerdesek = [konnyu_kerdes1, konnyu_kerdes2, konnyu_kerdes3, konnyu_kerdes4, konnyu_kerdes5, konnyu_kerdes6, konnyu_kerdes7]

#Normál
normal_kerdes1 = Kerdes("Egészítse ki a híres novella címét! 'Mario és a ...'","varázshegy","varázsló","kiválasztott","Buddenbrook-ház","B")
normal_kerdes2 = Kerdes("Ki rendezte a Titanic című 1997-ben készült filmet?", "Richard Donner", "Ron Howard", "Steven Spielberg", "James Cameron", "D")
normal_kerdes3 = Kerdes("Mennyi a fény terjedési sebessége levegőben, légüres térben?", "300.000 km/h", "300.000 km/s", "30.000 m/s", "150.000 m/s", "B")
normal_kerdes4 = Kerdes("Milyen állat a kazuár", "ausztráliai hüllő", "macskaféle", "futómadár", "medúza", "C")
normal_kerdes5 = Kerdes("A csicsóka melyik része ehető?", "virágzata", "levele", "gyökérgumója", "magja", "C")
normal_kerdes6 = Kerdes("Hol imádkoznak a buddhista szerzetesek?", "dzsámiban", "pagonyban", "pagodában", "minaretben", "C")
normal_kerdes7 = Kerdes("Kit szeretett 'forrón' Tony Curtis az 1959-es híres vígjátékban?", "Ava Gardenert", "Doris Dayt", "Marilyn Monroe-t", "Anita Ekberget","C")
normal_kerdes8 = Kerdes("Hol haladhat át a gyalogos a KRESZ szerint?", "híd úttestjén", "felüljáró úttestjén", "főútvonalon", "autópályán", "C")
normal_kerdes9 = Kerdes("Az alábbiak közül melyik nem magyar származási lófajta?", "kisbéri", "hucul", "fríz", "furioso", "C")
normal_kerdes10 = Kerdes("A felsoroltak közül, mi Görögország jellegzetes itala?", "beherovka", "vodka", "ouzo", "bor", "C")
normal_kerdesek = [normal_kerdes1, normal_kerdes2, normal_kerdes3, normal_kerdes4, normal_kerdes5, normal_kerdes6, normal_kerdes7, normal_kerdes8, normal_kerdes9, normal_kerdes10]

#Nehéz
nehez_kerdes1 = Kerdes("Mit neveztek régen indóháznak?", "telefonközpont", "kékfestőműhely", "vasútállomás", "autó motort", "C")
nehez_kerdes2 = Kerdes("Melyik Erkel-operában hangzik el a 'Palotás'?", "Sarolta", "Bánk bán", "Dózsa György", "Hunyadi László", "D")
nehez_kerdes3 = Kerdes("Milyen mára elavult jelentése volt évszázadokkal ezelőtt a 'marha' szónak?", "család", "vagyon", "ügyetlen lovas", "alattvaló", "B")
nehez_kerdes4 = Kerdes("Hányszor kell körbejárnia egy iszlám hívőnek Mekkában a Kába-követ?", "háromszor", "hétszer", "ötször", "tízszer", "B")
nehez_kerdes5 = Kerdes("Az alábbi történelmi alakok közül kit nem Ádám személyesít meg 'Az ember tragédiájában?'", "Miltiadész", "Kepler", "Michelangelo", "Danton", "C")
nehez_kerdes6 = Kerdes("Hogy hívják Indira Gandhi fiát, aki később szintén merénylet áldozata lett?", "Karamcsand Gandhi", "Radzsiv Gandhi", "Csaran Szingh", "Csandra Sékhar", "B")
nehez_kerdes7 = Kerdes("A felsoroltak közül melyik NEM Shakespeare műve?", "Elveszett paradicsom", "Szentivánéji álom","Sok hűhó semmiért","Ahogy tetszik","A")
nehez_kerdesek = [nehez_kerdes1, nehez_kerdes2, nehez_kerdes3, nehez_kerdes4, nehez_kerdes5, nehez_kerdes6, nehez_kerdes7]

def legyenonis(egyenleg):
    kerdesek_szama = 1
    print("Üdvözöllek a Legyen Ön Is Milliomos játékban!")
    segitsegek_lista = ["felezés", "közönség", "hívás"]
    #Könnyű
    for _ in range(5):
        kerdes = random.choice(konnyu_kerdesek)
        print(f"{kerdesek_szama}. kérdés:")
        if kerdesek_szama == 1:
            tet = 10000
        elif kerdesek_szama == 2:
            tet = 20000
        elif kerdesek_szama == 3:
            tet = 50000
        elif kerdesek_szama == 4:
            tet = 100000
        elif kerdesek_szama == 5:
            tet == 250000
        print(f"Tét: {tet}Ft")
        key = input(f"{kerdes.kerdes} \n A: {kerdes.a} \n B: {kerdes.b} \n C: {kerdes.c} \n D: {kerdes.d} \n ")
        kerdesek_szama+=1
        if key.upper() == kerdes.megoldas:
            print("helyes válasz")
            print("--------------------")
            konnyu_kerdesek.remove(kerdes)
        elif key.upper() == "SEGÍTSÉG" or key.upper() == "S":
            segitsegek(segitsegek_lista, kerdes)
        else:
            print(f"Helytelen választ adtál meg. A megoldás {kerdes.megoldas} volt.")
            lobby(egyenleg)
    #Normál
    for _ in range(5):
        kerdes = random.choice(normal_kerdesek)
        print(f"{kerdesek_szama}. kérdés:")
        if kerdesek_szama == 6:
            tet = 500000
            nyeremeny = 250000
        elif kerdesek_szama == 7:
            tet = 750000
        elif kerdesek_szama == 8:
            tet = 1000000
        elif kerdesek_szama == 9:
            tet = 1500000
        elif kerdesek_szama == 10:
            tet == 2000000
        print(f"Tét: {tet}Ft")
        key = input(f"{kerdes.kerdes} \n A: {kerdes.a} \n B: {kerdes.b} \n C: {kerdes.c} \n D: {kerdes.d} \n ")
        kerdesek_szama+=1
        if key.upper() == kerdes.megoldas:
            print("helyes válasz")
            print("--------------------")
            normal_kerdesek.remove(kerdes)
        elif key.upper() == "SEGÍTSÉG" or key.upper() == "S":
            segitsegek(segitsegek_lista)
        else:
            print(f"Helytelen választ adtál meg. A megoldás {kerdes.megoldas} volt.")
            lobby(egyenleg)
    #Nehéz
    for _ in range(5):
        kerdes = random.choice(nehez_kerdesek)
        print(f"{kerdesek_szama}. kérdés:")
        if kerdesek_szama == 11:
            tet = 5000000
        elif kerdesek_szama == 12:
            tet = 10000000
        elif kerdesek_szama == 13:
            tet = 15000000
        elif kerdesek_szama == 14:
            tet = 25000000
        elif kerdesek_szama == 15:
            tet == 	50000000
        elif kerdesek_szama == 16:
            nyeremeny = 50000000
            print(f"Nyertél! Gratulálok! Nyereményed: {nyeremeny}Ft")
        print(f"Tét: {tet}Ft")
        key = input(f"{kerdes.kerdes} \n A: {kerdes.a} \n B: {kerdes.b} \n C: {kerdes.c} \n D: {kerdes.d} \n ")
        kerdesek_szama+=1
        if key.upper() == kerdes.megoldas:
            print("helyes válasz")
            print("--------------------")
            nehez_kerdesek.remove(kerdes)
        elif key.upper() == "SEGÍTSÉG" or key.upper() == "S":
            segitsegek(segitsegek_lista)
        else:
            print(f"Helytelen választ adtál meg. A megoldás {kerdes.megoldas} volt.")
            lobby(egyenleg)
=======
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
 
>>>>>>> a14f8a85954e57a2837951be7c070056b0fe25a3
lobby(egyenleg)