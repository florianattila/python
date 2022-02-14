szo = input("Írj be egy szót")
def névelő(szó):
    magánhangzók= ["a", "á", "e", "é", "i", "í", "o", "ó", "ö", "ő", "u", "ú", "ü", "ű", "y"]
    if szó[0] in magánhangzók:
        return "az"
    else:
        return "a"

print(névelő(szo), szo)

ft = int(input("Adj meg pénzt"))
benzin = 480 
veszel = ft/benzin
print(f"{ft}ft-ből {veszel:.2f}l benzint veszel:(")

