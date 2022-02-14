a= "Helló, Világ!"
tt = a.upper()
print(tt)

a = "Hello, World!"
print(a.lower())

#A replace()módszer egy karakterláncot egy másik karakterlánccal helyettesít:
a = "Hello, World!"
print(a.replace("H", "J"))

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

#A strip()módszer eltávolítja a szóközöket az elejéről vagy a végéről:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


#A split()metódus részláncokra osztja a karakterláncot, ha megtalálja az elválasztó példányait:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Konkatenáció
a = "Hello"
b = "World"
c = a + b
print(c)

#Ha szóközt szeretne hozzáadni közéjük, adjon hozzá egy " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)

gyumolcs = "banán"
m = gyumolcs[1]
print(m)

m = gyumolcs[0]
print(m)