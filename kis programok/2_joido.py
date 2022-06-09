szombat = int(input("Hány fok volt szombaton?"))
vasarnap = int(input("Hány fok volt vasarnap?"))

def melegebb(szombat, vasarnap):
    if vasarnap > szombat:
        return f"Vasárnap melegebb volt, {vasarnap}°C volt"
    elif szombat > vasarnap:
        return f"Szombaton melegebb volt, {szombat}°C volt"
    else:
        return "Egyenlő"

print(melegebb(szombat, vasarnap))