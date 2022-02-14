import random

<<<<<<< HEAD
=======
#verzió: Béta v2.1
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
#változók definiálása
tipp = None
gondoltam = None
kategoria = None
rakerdezel = None
<<<<<<< HEAD
=======
proba = None
nehezseg = None
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f

#függvények és eljárások
def ellenorzes(tipp):
    if tipp == gondoltam[kategoria] or tipp in gondoltam[kategoria]:
        print("talált")
    else:
        print("nem talált")

def alahuzas (jel):
    for _ in range(10):
        print(jel, end="")
    print("")

#állatok kategóriái
kutya = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "közepes",
    "táplálkozás" : "ragadozó",
    "szelídített":"házi",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "barna", "fehér", "szürke"],
<<<<<<< HEAD
=======
    "fog" : "van",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
}

macska = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "kicsi",
    "táplálkozás" : "ragadozó",
    "szelídített":"házi",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "barna", "fehér", "szürke"],
<<<<<<< HEAD
}

aranyhal = {
    "él" : "víz",
    "lábai száma" : "0",
    "méret" : "kicsi",
    "táplálkozás" : "mindenevő",
    "szelídített":"házi",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["arany"],
=======
    "fog" : "van",
    "toll" : "nincs",
}

ponty = {
    "él" : "víz",
    "lábai száma" : "0",
    "méret" : "közepes",
    "táplálkozás" : "mindenevő",
    "szelídített":"vad",
    "osztály" : "hal",
    "törzs" : "gerinchúros",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["barna"],
    "fog" : "nincs",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
}

légy = {
    "él" : "levegő",
    "lábai száma" : "6",
    "méret" : "apró",
    "táplálkozás" : "mindenevő",
    "szelídített":"háztályi",
    "osztály" : "rovar",
    "törzs" : "ízeltlábú",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "szürke"],
<<<<<<< HEAD
=======
    "fog" : "nincs",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
}

galamb = {
    "él" : "levegő",
    "lábai száma" : "2",
    "méret" : "kicsi",
    "táplálkozás" : "mindenevő",
<<<<<<< HEAD
    "szelídített":"házitályi",
=======
    "szelídített":"háztályi",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    "osztály" : "madár",
    "törzs" : "gerinces",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fehér","szürke"],
<<<<<<< HEAD
=======
    "fog" : "nincs",
    "toll" : "van",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

polip = {
    "él" : "víz",
    "lábai száma" : "0",
    "méret" : "közepes",
    "táplálkozás" : "ragadozó",
    "szelídített":"vad",
    "osztály" : "fejlábú",
    "törzs" : "puhatestű",
    "szárny" : "nincs",
    "kar" : "van",
    "veszélyes" : "nem",
    "szín" : ["barna", "narancssárga", "vörös"],
<<<<<<< HEAD
=======
    "fog" : "nincs",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

majom = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "közepes",
    "táplálkozás" : "mindenevő",
    "szelídített":"vad",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "van",
    "veszélyes" : "nem",
    "szín" : ["fekete", "barna", "szürke", "bőrszín"],
<<<<<<< HEAD
=======
    "fog" : "van",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

csirke = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "kicsi",
    "táplálkozás" : "növényevő",
    "szelídített":"házi",
    "osztály" : "madár",
    "törzs" : "gerinces",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "barna", "fehér", "citromsárga"],
<<<<<<< HEAD
=======
    "fog" : "nincs",
    "toll" : "van",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

csiga = {
    "él" : "szárazföld",
    "lábai száma" : "0",
    "méret" : "kicsi",
    "táplálkozás" : "növényevő",
<<<<<<< HEAD
    "szelídített":"házitályi",
=======
    "szelídített":"háztályi",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    "osztály" : "csigák",
    "törzs" : "puhatestű",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["bőrszín", "barna"],
<<<<<<< HEAD
=======
    "fog" : "nincs",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

méh = {
    "él" : "levegő",
    "lábai száma" : "6",
    "méret" : "apró",
    "táplálkozás" : "növényevő",
<<<<<<< HEAD
    "szelídített":"házitályi",
=======
    "szelídített":"háztályi",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    "osztály" : "rovarok",
    "törzs" : "ízelt lábú",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "igen",
    "szín" : ["fekete", "sárga"],
<<<<<<< HEAD
=======
    "fog" : "nincs",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

lajhár = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "közepes",
    "táplálkozás" : "növényevő",
    "szelídített":"vad",
    "osztály" : "emlős",
<<<<<<< HEAD
    "törzs" : "gerices",
=======
    "törzs" : "gerinces",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    "szárny" : "nincs",
    "kar" : "van",
    "veszélyes" : "nem",
    "szín" : ["barna"],
<<<<<<< HEAD
=======
    "fog" : "van",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

ló = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "nagy",
    "táplálkozás" : "növényevő",
    "szelídített":"házi",
    "osztály" : "emlős",
<<<<<<< HEAD
    "törzs" : "gerices",
=======
    "törzs" : "gerinces",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "barna", "fehér", "szürke"],
<<<<<<< HEAD
=======
    "fog" : "van",
    "toll" : "nincs",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    }

pingvin = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "közepes",
    "táplálkozás" : "ragadozó",
    "szelídített":"vad",
    "osztály" : "madár",
<<<<<<< HEAD
    "törzs" : "gerices",
=======
    "törzs" : "gerinces",
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "fehér"],
<<<<<<< HEAD
    }

allatok = [kutya, macska, aranyhal, galamb, légy, polip, majom, csirke, csiga, méh, ló, pingvin]
allatszamlista = [0,1,2,3,4,5,6,7,8,9,10,11]
megoldaslista = ["kutya", "macska", "aranyhal", "galamb", "légy", "polip", "majom", "csirke", "csiga", "méh", "ló", "pingvin"]

#szabályok
alahuzas("~")
print("     --SZABÁLYOK--     ")
print("1. három alkalommal kérdezhetsz rá, ha harmadjára sem sikerül eltalálnod az állatot, akkor kiesel.")
print("2.Választhatsz nehézséget \n könnyű = 3 próba \n közepes = 2 próba \n nehéz = 1 próba")
print("3. A kategorizálások az alábbiak: \n él : szárazföld/ víz/ levegő  \n lábai száma : 0/2/4, \n méret : apró (pl. bogár), kicsi (pl tyúk), közepes (pl. kutya), nagy (pl. zsiráf)  \n táplálkozás : ragadozó/ növényevő/mindenevő \n szelídített : házi/ háztályi/ vad \n osztály : emlős/csigák/madár/stb. \n törzs : gerinces/ puhatestű/stb. \n szárny : nincs/van \n kar : nincs/van \n veszélyes : igen/nem \n szín : NINCS ÁRNYALAT")
alahuzas("~")

#
nehezseg = input("válasszon nehézséget")
if nehezseg == "könnyű":
    proba = 3
elif nehezseg == "közepes":
    proba = 2
elif nehezseg == "nehez":
    proba = 1
=======
    "fog" : "nincs",
    "toll" : "van",
    }

cápa = {
    "él" : "víz",
    "lábai száma" : "0",
    "méret" : "nagy",
    "táplálkozás" : "ragadozó",
    "szelídített":"vad",
    "osztály" : "hal",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "igen",
    "szín" : ["szürke", "fehér"],
    "fog" : "van",
    "toll" : "nincs",
    }

kacsa = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "kicsi",
    "táplálkozás" : "mindenevő",
    "szelídített":"házi",
    "osztály" : "madár",
    "törzs" : "gerinces",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["szürke", "fehér"],
    "fog" : "nincs",
    "toll" : "van",
    }

medve = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "nagy",
    "táplálkozás" : "ragadozó",
    "szelídített":"vad",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "igen",
    "szín" : ["barna"],
    "fog" : "van",
    "toll" : "nincs",
    }

zsiráf = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "nagy",
    "táplálkozás" : "növényevő",
    "szelídített":"vad",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["sárga"],
    "fog" : "van",
    "toll" : "nincs",
    }

kecske = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "közepes",
    "táplálkozás" : "növényevő",
    "szelídített":"házi",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyess" : "nem",
    "szín" : ["fehér", "barna"],
    "fog" : "van",
    "toll" : "nincs",
    }

tehén = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "nagy",
    "táplálkozás" : "növényevő",
    "szelídített":"házi",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["barna","fehér", "fekete", "szürke"],
    "fog" : "van",
    "toll" : "nincs",
    }

bálna = {
    "él" : "víz",
    "lábai száma" : "0",
    "méret" : "nagy",
    "táplálkozás" : "ragadozó",
    "szelídített":"van",
    "osztály" : "emlős",
    "törzs" : "gerinces",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["kék", "fehér", "szürke"],
    "fog" : "van",
    "toll" : "nincs",
    }

allatok = [kutya, macska, ponty, galamb, légy, polip, majom, csirke, csiga, méh, ló, pingvin, cápa, kacsa, medve, zsiráf, kecske, tehén, bálna]
allatszamlista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
megoldaslista = ["kutya", "macska", "ponty", "galamb", "légy", "polip", "majom", "csirke", "csiga", "méh", "ló", "pingvin", "cápa", "kacsa","medve", "zsiráf","kecske","tehén", "bálna"]

#szabályok
alahuzas("~")
print("     ---SZABÁLYOK---     ")
print("1. három alkalommal kérdezhetsz rá, ha harmadjára sem sikerül eltalálnod az állatot, akkor kiesel.")
print("2. Ha rákérdezés közben a 'próbáim száma' szöveggel tudhatod meg mennyi próbád maradt.")
print("3. A kategorizálások az alábbiak: \n él : szárazföld/ víz/ levegő  \n lábai száma : 0/2/4, \n méret : apró (pl. bogár), kicsi (pl tyúk), közepes (pl. kutya), nagy (pl. zsiráf)  \n táplálkozás : ragadozó/ növényevő/mindenevő \n szelídített : házi/ háztályi/ vad \n osztály : emlős/csigák/madár/stb. \n törzs : gerinces/ puhatestű/stb. \n szárny : nincs/van \n kar : nincs/van \n veszélyes : igen/nem \n szín : NINCS ÁRNYALAT \n fog : van/nincs \n toll : van/nincs")
alahuzas("~")

#Nehézsé
nehezseg = input("\nVálasszon nehézséget: könnyű (3 próba), közepes (2 próba), nehéz (1 próba)!")
if nehezseg == "könnyű":
    proba = 3
elif nehezseg == "közepes":
    proba == 2
elif nehezseg == "nehéz":
    proba = 1
else:
    print("Nincs ilyen nehézség")

    

>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f

#Játék
allatszam = random.choice(allatszamlista)
gondoltam = allatok[allatszam]
megoldas = megoldaslista[allatszam]
print("\n Gondoltam egy állatra")

while proba != 0:   
    while rakerdezel != "igen":
        kategoria = input("Írd be a tipped kategóriáját!")
        tipp = input("Írd be a tipped!")
        ellenorzes(tipp)
        rakerdezel = input("Rá szeretnél kérdezni a megoldásra?")
    rakerdez = input("Mit gondolsz, mi a megoldás?")
    if rakerdez == megoldas:
        print("nyertél, ügyes vagy")
<<<<<<< HEAD
=======
    elif rakerdez == "próbáim száma":
        print(f"{proba} próbád maradt.")
>>>>>>> 71779ab0d47ecb3fb51938b62aa3ba421f227e4f
    else:
        proba -= 1
        print(proba, " próbálkozási lehetőséged maradt.")
print("Kiestél, majd máskor jobban megy. A megoldás", megoldas, "volt")
proba = 3