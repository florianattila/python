import random
egyik = random.randint(1,10)
másik = random.randint(1,10)
összeg = egyik+másik
print(összeg)
if összeg%2 == 0:
    print("páros")
    if összeg%3 == 0:
        print("osztható 3-mal")
    else:
        print("nem osztható 3-mal")
else:
    print("páratlan")