diak = {
    'vezeteknev': 'Kiss',
    'keresztnev': 'Péter',
    'osztaly': '10.A',
    'eletkor': 17,
    'cim': {
          'iranyitoszam': 9400,
          'varos': 'Sopron',
          'kozterulet': 'Fő utca',
          'hazszam': 5
    }
}
print(diak['cim']['iranyitoszam'])

#videó

diak = {
    "vezeteknev" : "Kiss",
    "keresztnev" : "Péter",
    "eletkor": 17,
    "menza": True
    "matek_jegyek":[5,4,4,3,5,5]
}
del diak["vezeteknev"]
print(diak)
print(diak.values())
for ertek in diak.values():
    print(ertek)
print(diak.items())
for kulcs, ertek in diak.items():
    print(kulcs, ertek)