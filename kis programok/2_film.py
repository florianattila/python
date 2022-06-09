def kiir(ora, perc):
    return str(ora) + "ora " + str(perc) + "perc hosszű" 

def oraperc(hossz):
    ora = hossz//60
    perc = hossz-ora *60
    return kiir(ora, perc) 

for _ in range(3):
    cim = input("Adjon meg egy film címet")
    hossz = int(input("Adja meg a film hosszát"))
    print(f"A(z) {cim} című film {oraperc(hossz)}, ({hossz}perc)")
