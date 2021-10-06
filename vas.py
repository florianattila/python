PA = 105
OLVADAS = 1539
FORRASPONT = 2750
vas = int(input("Milyen hőfok?"))
if vas < PA:
    print("Szilárd")
elif vas < OLVADAS:
    print ("Folyékony")
else:
    print("Gáz")