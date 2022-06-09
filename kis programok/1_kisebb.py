wr = open("kisebb.txt", "w")
szam1 = int(input("Adj meg egy számot!"))
szam2 = int(input("Adj meg egy másik számot!"))
if szam1 > szam2:
    print(f"{szam2} kisebb")
    wr.write(f"{szam2} kisebb")
elif szam2 > szam1:
    print(f"{szam2} nagyobb")
    wr.write(f"{szam2} nagyobb")
else:
    print("A két szám egyenlő")
    wr.write("A két szám egyenlő")