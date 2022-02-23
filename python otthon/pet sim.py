allat = {
    "név": "",
    "típus" : "",
    "kor" : 0,
    "éhség" : 0,
    "játékok" : []
}

def kilepes():
    return "Vége a játéknak. Köszönöm hogy játszottál!"
    

def etetes():
    ujehseg = allat["éhség"]
    if ujehseg < 0:
        ujehseg = 0
    allat["éhség"]= ujehseg
    print("Megetetted az állatod")

jatekok = {
    "macska" : ["játék egér", "kaparófa", "cérna"],
    "kutya" : ["bot","frizbi","rágójáték"],
    "hal" : ["vízalatti kastély","korall","tengeri kincs"]
}

def jatekszerzes():
    jatekvalasztas = jatekok[allat["típus"]]
    jatekszama =-1
    while jatekszama < 0 or jatekszama > len(jatekok):
        print("Válassz: ")
        for i in range(len(jatekvalasztas)):
            print(f"{str(i)}: {jatekvalasztas[i]}")
        
        jatekszama =int(input("Kérlek írd be a választott játék számát: "))
    valasztottjatek = jatekvalasztas[jatekszama]
    allat["játékok"].append(valasztottjatek)
    print(f"Sikeresen kiválasztottad a(z) {valasztottjatek} játékot!")

def allatvalasztas():
    allattipus = ""
    allatopciok = list(jatekok.keys())
    while allattipus not in allatopciok:
        for opciok in allatopciok:
            print(opciok)
        allattipus = input("Milyen állatot szeretnél?")
    allat["típus"] = allattipus
    print("Sikeresen kiválasztottad az állatod!")

def elnevezes():
    allatnev = ""
    allatnev = input("Add meg az állatod nevét! ")
    allat["név"] = allatnev

def Menu(menuopciok):
    opciogomb = list(menuopciok.keys())
    print("Ezek a választási lehetőségek: ")
    print("--------------")
    for key in opciogomb:
        print(key + ":\t" + menuopciok[key]["text"])

def jatek():
    allatvalasztas()
    menuopciok = {
        "Q" : {"function":kilepes(), "text": "Kilépés a játékból"},
        "F" : {"function": etetes(), "text": allat["nev"] + " etetése"},
    }
    Menu(menuopciok)

jatekfut = True
while jatekfut:
    menuvalasztas = ""
    #while menuvalasztas not in menuopciok.keys():
    #    Menu(menuopciok)