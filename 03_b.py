#!/usr/bin/env python3

# Olvassuk be, hogy hány picula egy mütyürke nettó ára, majd írjuk ki
# a bruttó árakat a német (19%), a brit (20%), a cseh (21%),
# a lengyel (23%) és a magyar áfakulcs használatával!
# Az áfakulcsok számértékét adjuk meg "konstansok" használatával!

NÉMET = 19
BRIT = 20
CSEH = 21
LENGYEL = 23
MAGYAR = 27

nettó_ár = float(input('Hogyér\' adnak egy mütyürkét? '))
print(f'A mütyürke bruttó árai:')
print(f'{nettó_ár*(1+NÉMET/100):10.2f} picula Németországban.')
print(f'{nettó_ár*(1+BRIT/100):10.2f} picula a ködösben.')
print(f'{nettó_ár*(1+CSEH/100):10.2f} picula Švejk hazájában.')
print(f'{nettó_ár*(1+LENGYEL/100):10.2f} picula a másik jóbarátnál.')
print(f'{nettó_ár*(1+MAGYAR/100):10.2f} picula Magyarországon.')
# 
# kipróbálandó formázások
# semmi
# :5.2f
print(f'{nettó_ár*(1+NÉMET/100):5.2f} picula Németországban.')
# írjuk át a BRIT-et 20100-ra
# 10.2f
# <10.2f
print(f'{nettó_ár*(1+NÉMET/100):<10.2f} picula Németországban.')
# ^10.2f
print(f'{nettó_ár*(1+NÉMET/100):^10.2f} picula Németországban.')
