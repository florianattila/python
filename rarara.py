import random
a = random.randint(1,3)
tipp = int(input("Gondoltam egy számra 1 és 3 közt, tippelj!"))
if tipp == a:
    print("Ügyes vagy!")
else:
    print(a, "Volt a helyes:(")