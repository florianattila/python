#list comprehensions
szamok = [x for x in range (20)]
print(szamok)

paros = [x for x in range (20) if x%2 == 0]
print(paros)
paratlan = [x for x in range(20) if x%2 !=0]
print(paratlan)

nevek = ["andi", "karcsi", "jozsef", "zsofi", "eniko"]
nevek = [nev.capitalize() for nev in nevek]
print(nevek)

nevek_A = [nev for nev in nevek if nev.startswith("A")]
print(nevek_A)

#Nehezebb
matrix0 = [[0 for x in range(4)]for y in range(4)]
matrix_print =lambda matrix: [print(row) for row in matrix]
matrix_identity = [[1 if x==y else 0 for x in range(4)]for y in range(4)]
matrix_print(matrix_identity)