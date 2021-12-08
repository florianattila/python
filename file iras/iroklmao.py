#klasszikus
#írás
wr = open("10b", "w")
wr.write("lmao")
wr.close()

#olvasás
wr = open("10b", "r")
tartalom = wr.read()
print(tartalom)
wr.close()


#hozzáírás
wr = open("10b", "a")
wr.write("xd")
wr.close()



#kontextuskezelő
#írás
with open("10b", "w", encoding="utf-8") as file:
    file.write("10vbucks")

#olvasás
with open("10b", "r", encoding="utf-8") as file:
    file.write("20vbucks")