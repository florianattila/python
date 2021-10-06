egyik = int(input("Adjon meg egy számot!"))
masik = int(input("Adjon meg egy másik számot is!"))
jel = input("Adjon meg egy műveleti jelet")
#print("A művelet eredménye: ", end = "")
if jel == "+":
    print(egyik+masik)
elif jel == "-":
    print(egyik-masik)
elif jel == "*":
    print(egyik*masik)
elif jel == "%":
    print(egyik%masik)
elif jel == ">>":
    print(egyik>>masik)
elif jel == "<<":
    print(egyik<<masik)
elif jel == "/":
    print(egyik/masik)