kedd = int(input("Mennyit költöttél kedden?"))
szerda = int(input("Mennyit költöttél szerdán?"))
"""
if szerda < kedd:
    print(f"kedden többet költöttél, {kedd-szerda}val")
elif szerda > kedd:
    print(f"szerdán többet költöttél, {szerda-kedd}val")
else:
    print(f"Ugyanannyit költöttél")
"""
def koltes(kedd, szerda):
    if szerda < kedd:
        return f"kedden többet költöttél, {kedd-szerda}val"
    elif szerda > kedd:
        return f"szerdán többet költöttél, {szerda-kedd}val"
    else:
        return f"Ugyanannyit költöttél"

koltes(kedd,szerda)