#Dekoráló függvény
def validate_div(func):
    def wrapper(value1, value2):
        if value2 == 0:
            return "Nem oszthatsz nullával!"
        return func(value1, value2)
    return wrapper

#Dekorált függvény
@validate_div
def divide(value1, value2):
    return value1/value2

print(divide(5, 0))

def validate_form(func):
    def wrapper(password, email):
        if len(password) < 6:
            return "Gyenge a jelszó, legalább 6 karakter"
        if "@" not in email:
            return "Nem érvényes email"
        return func(password, email)
    return wrapper

@validate_form
def form(password, email):
    return "A jelszavad elég erős, és érvényes email címed van"

print(form("1212", "ati"))
print(form("555555555", "ati@gmail.com"))

#Két dekorátor
def email_hitelesítés(fuggveny):
    def ellenorzes(email, password):
        if "@" not in email:
            return "Nem érvényes email"
        return fuggveny(email, password)
    return ellenorzes

def jelszo_hitelesítés(fuggveny):
    def ellenorzes(email, password):
        if len(password) < 6:
            return "Gyenge a jelszó, legalább 6 karakter "
        return fuggveny(email, password)
    return ellenorzes

@email_hitelesítés
@jelszo_hitelesítés
def vegso(email, password):
    return "A jelszavad elég erős, és érvényes email címed van"

print(vegso("ati@gmail.com", "555555555"))