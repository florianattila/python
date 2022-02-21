#closure

from sqlite3 import OperationalError


def kulso():
    szam = 21
    def belso():
        nonlocal szam #nonlocal nélkül is eléri a változót, de nem módosíthatja
        szam+=1 
        print(szam)
    return belso

# A belső függvény használja a külső értéket
def op_factory(oper,num):
    def operation(value):
        if oper == "**":
            return value ** num
        elif oper == "*":
            return value * num
        elif oper == "/" :
            return value / num
        else:
            return "Not supported operator"

    return operation

osztas = op_factory("/", 5)
negyzet = op_factory("**", 2)
kob = op_factory("**", 3)
hiba = op_factory("$", 5)
print(negyzet(5))
print(kob(5))
print(osztas(10))
print(hiba(5))