bulizok = int(input("bulizók"))
rendor = int(input("rendőrök"))
if rendor == 0:
    print("Minden bulizó megmenekült")
else:
    elkapottak = 0
    for i in range(1, rendor + 1):
        elkapottak +=i
    if elkapottak < bulizok:
        elmenekult = bulizok - elkapottak
        print(elkapottak, "bulizót kaptak el,", elmenekult, "pedig elmenekült")
    else:
        print("Ajaj, mindenkit elkaptak")