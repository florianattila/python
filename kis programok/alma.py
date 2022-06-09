def vonalkod(kod):
    if kod == 599:
        return True
    else:
        return False

nev = "asdfghjklll"
while nev:
    nev = input("Add meg a vásárló nevét! ")
    if nev:
        kod = int(input("Add meg a gyümölcs vonalkódjának első három számát ! "))
        if vonalkod(kod):
            print(f"{nev} magyar gyümölcsöt vásárolt. ")
        else:
            print(f"{nev} nem magyar gyümölcsöt vásárolt. ")