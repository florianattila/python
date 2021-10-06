kor = int(input("Adja meg a korát"))
if kor < 13:
    print("gyermek")
elif kor < 17:
    print("fiatalkorú")
elif kor < 23:
    print("ifjú")
elif kor < 59:
    print("felnőtt")
elif kor > 60:
    print("idős")