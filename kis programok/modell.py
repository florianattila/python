kor = int(input("Adja meg az életkorát "))
nev = input("Adja meg a nevét ")
magassag = int(input("Adja meg a magasságát "))

if kor < 20:
    print("Ez a modell még csitri")
elif kor > 20:
    print("Ez a modell vén") 
else:
    print("Kiváló")
        

if magassag >= 170 and magassag <= 175:
    print("A modell alkalmazható") 
else:
    print("Elutasítva")