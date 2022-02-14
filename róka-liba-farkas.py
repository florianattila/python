libák = [1,5,2,3,4]
róka = 0
farkas = 0
for liba in libák:
    if liba > 3:
        farkas = farkas+liba
    else:
        róka = róka+liba
print(f"a róka {róka}kg, a farkas meg {farkas}kg libát evett.")