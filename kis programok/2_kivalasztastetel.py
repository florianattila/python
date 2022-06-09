t = [3, 8, 2, 4, 5, 1, 6]
n = len(t)
ker = int(input("Melyik számot keressem?"))
i = 0
while t[i] != ker:
    i += 1
print("Hanyadik helyen van:", i+1)

i = 0
while i <n and t[i] != ker:
    i +=1

if(i < n):
    print("Van " + str(ker) + " elem")
    print("Helye: ", i+1)
else:
    print("Nincs")

