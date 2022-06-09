class HíresFilm:
    def __init__(self, cim, hossz, nemzetiseg):
        self.cim = cim
        self.hossz = hossz
        self.nemzetiseg = nemzetiseg
    def nemzetisegek(self):
        if self.nemzetiseg == "USA":
            return "amerikai"
        elif self.nemzetiseg == "GB":
            return "angol"

filmek = []
for _ in range(3):
    cim = input("Add meg egy híres film címét! ")
    hossz= int(input("Add meg a hosszát!"))
    nemzet = input("Add meg a nemzetiségét (GB/USA)!")
    film = HíresFilm(cim, hossz, nemzet)
    filmek.append(film)

for x in filmek:
    print(f"{x.cim} egy híres {x.hossz} perces {x.nemzetisegek()} film.")