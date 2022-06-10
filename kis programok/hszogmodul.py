import math

def hkerulet(a,b,c):
    return a+b+c

def hterulet(a,b,c):
    s = hkerulet(a,b,c)/2
    return s*(math.sqrt(s-a)*(s-b)*(s-c))

kerulet = {
    "haromszog" : lambda a,b,c : a+b+c,
    "negyszog" : lambda a,b,c,d : a+b+c+d,
    "negyzet" : lambda a : a*4,
}

terulet = {
    "haromszog" : lambda a,b,c : (a+b+c/2)*(math.sqrt((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c)),
    "negyzet" : lambda a : a**2,
}

