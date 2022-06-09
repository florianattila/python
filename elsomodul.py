import math

def korterulet(r):
    return r**2*math.pi

def korkerulet(r):
    return r*2*math.pi

def haromszogkerulet(a,b,c):
    return a+b+c

def haromszogterulet(a,b,c):
    s = a+b+c/2
    return math.sqrt(s(s-a)(s-b)(s-c))