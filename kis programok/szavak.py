egyik = input("Add meg a szót")
egyik_hossz = len(egyik)
masik = input("Add meg a szót")
masik_hossz = len(masik)

def nagyobb(egyik, masik, egyik_hossz, masik_hossz):
    if egyik_hossz > masik_hossz:
        print(f"Az első ({egyik}) szó hosszabb mint a második ({masik})")
    elif masik_hossz > egyik_hossz:
        print(f"A második ({masik}) szó hosszabb mint az első ({egyik})")
    else:
        print("A két szó ugyanolyan hosszú")

nagyobb(egyik, masik, egyik_hossz,masik_hossz)