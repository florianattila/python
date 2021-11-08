nev = input("Adja meg a nevét! ")
kor = int(input("Adja meg a korát"))
while kor > 18 or kor < 0:
    print("0 és 18 közti számot adjon  meg")
    kor = int(input("Adja meg a korát"))

if kor <=3:
    print(f"{kor}évesen :Totyogóknak a kettes számrendszerről")
elif kor <= 6:
    print(f"{kor}évesen :Hackeljük meg az óvodát!")
elif kor <= 14:
    print(f"{kor}évesen :Felhőtechnológia a menzán")
elif kor <= 18:
    print(f"{kor}évesen :Big data a középiskolában")