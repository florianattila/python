import random
honap = ["január", "február", "március", "április", "május"]
for i in honap:
    print(i, end=" ")
print("\nA tömb mérete: ", len(honap))
for j in range (len(honap)):
    print("%d. hónap: %s" % (j+1, honap[j]))
print(random.choice(honap))

str1 = "isz"
hb = ""
hb = "h" + str1 + "ed"
print (hb)
print(hb[3])
hb[0]= "v"

str1 = "hiszed"
print(len(str1))
print(str1[1:4])
str1 = str1[1:]
print(str1)
str1 = str1[:3]+"o"+str1[:4]
print(str1)