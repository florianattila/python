import math

r = float(input("Adja meg a kör sugarát! "))
t = r*r*math.pi
print(f" A kör területe {t}")

a = float(input("Adja meg az a oldalt"))
b = float(input("Adja meg az b oldalt"))
c = float(input("Adja meg az c oldalt"))
mc = math.sqrt((a+b+c)*(-a+b+c)*(a-b+c)*(a+b-c))/2
k = a+b+c
t = (c*mc)/2
print(f"A háromszög kerülete: {k}. A háromszög területe: {t}")