my_list=[1,2,3,4,5,"abc", "def"]
with open("your_file.txt", "w") as file:
    for item in my_list:
        file.write("%s\n" % item)


f= open("your_file.txt")
tartalom = f.read()
print(tartalom)
f.close()