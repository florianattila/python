szo1 = input("Szót ")
szo2 = input("szót2 ")
if len(szo1) > len(szo2):
    print(szo1, "hosszabb")
elif len(szo1) < len(szo2):
    print(szo2, "hosszabb")
else:
    print("ugyanolyan hosszú")
