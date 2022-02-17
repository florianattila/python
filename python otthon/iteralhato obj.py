# iterable unpacking

rangelista1 = range(10)
print(list(rangelista1))
print(*rangelista1)

lista1 = [1,2,3,4]
lista2 = [*lista1] #Csillag nélkül ugyan azok lesznek, nem lehet csak az egyiket változtatni 

lista2[0] = 787
print(lista1)
print(lista2)

def func(*args, **kwargs):
    print(args)
    print(kwargs)
func(10,20,30,40, **{"nev1":"Andi","nev2":"Aniko"})

nevek = ["Gabor","Janos", "Arpad","Jozsef"]
korok = [14, 52, 62, 14]
nev_kor = [*nevek],[*korok]
print(nev_kor)