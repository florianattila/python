import random

#változók definiálása
tipp = None
gondoltam = None
kategoria = None
rakerdezel = None

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
    "szín" : ["fekete", "barna", "fehér", "szürke"]
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
    "szín" : ["fekete", "barna", "fehér", "szürke"]
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
    "szín" : ["arany"]
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
    "szín" : ["fekete", "szürke"]
}

galamb = {
    "él" : "levegő",
    "lábai száma" : "2",
    "méret" : "kicsi",
    "táplálkozás" : "mindenevő",
    "szelídített":"házitályi",
    "osztály" : "madár",
    "törzs" : "gerinces",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fehér","szürke"]
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
    "szín" : ["barna", "narancssárga", "vörös"]
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
    "szín" : ["fekete", "barna", "szürke", "bőrszín"]
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
    "szín" : ["fekete", "barna", "fehér", "citromsárga"]
    }

csiga = {
    "él" : "szárazföld",
    "lábai száma" : "0",
    "méret" : "kicsi",
    "táplálkozás" : "növényevő",
    "szelídített":"házitályi",
    "osztály" : "csigák",
    "törzs" : "puhatestű",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["bőrszín", "barna"]
    }

méh = {
    "él" : "levegő",
    "lábai száma" : "6",
    "méret" : "apró",
    "táplálkozás" : "növényevő",
    "szelídített":"házitályi",
    "osztály" : "rovarok",
    "törzs" : "ízelt lábú",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "igen",
    "szín" : ["fekete", "sárga"]
    }

lajhár = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "közepes",
    "táplálkozás" : "növényevő",
    "szelídített":"vad",
    "osztály" : "emlős",
    "törzs" : "gerices",
    "szárny" : "nincs",
    "kar" : "van",
    "veszélyes" : "nem",
    "szín" : ["barna"]
    }

ló = {
    "él" : "szárazföld",
    "lábai száma" : "4",
    "méret" : "nagy",
    "táplálkozás" : "növényevő",
    "szelídített":"házi",
    "osztály" : "emlős",
    "törzs" : "gerices",
    "szárny" : "nincs",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "barna", "fehér", "szürke"]
    }

pingvin = {
    "él" : "szárazföld",
    "lábai száma" : "2",
    "méret" : "közepes",
    "táplálkozás" : "ragadozó",
    "szelídített":"vad",
    "osztály" : "madár",
    "törzs" : "gerices",
    "szárny" : "van",
    "kar" : "nincs",
    "veszélyes" : "nem",
    "szín" : ["fekete", "fehér"]
    }

allatok = [kutya, macska, aranyhal, galamb, légy, polip, majom, csirke, csiga, méh, ló, pingvin]
allatszamlista = [0,1,2,3,4,5,6,7,8,9,10,11]
megoldaslista = ["kutya", "macska", "aranyhal", "galamb", "légy", "polip", "majom", "csirke", "csiga", "méh", "ló", "pingvin"]

#szabályok
alahuzas("~")
print("     --SZABÁLYOK--     ")
print("1. három alkalommal kérdezhetsz rá, ha harmadjára sem sikerül eltalálnod az állatot, akkor kiesel.")
print("2. A kategorizálások az alábbiak: \n él : szárazföld/ víz/ levegő  \n lábai száma : 0/2/4, \n méret : apró (pl. bogár), kicsi (pl tyúk), közepes (pl. kutya), nagy (pl. zsiráf)  \n táplálkozás : ragadozó/ növényevő/mindenevő \n szelídített : házi/ háztályi/ vad \n osztály : emlős/csigák/madár/stb. \n törzs : gerinces/ puhatestű/stb. \n szárny : nincs/van \n kar : nincs/van \n veszélyes : igen/nem \n szín : NINCS ÁRNYALAT")
alahuzas("~")

#Játék
proba = 3
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
    else:
        proba -= 1
        print(proba, " próbálkozási lehetőséged maradt.")
print("Kiestél, majd máskor jobban megy. A megoldás", megoldas, "volt")
proba = 3