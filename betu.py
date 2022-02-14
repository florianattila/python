def betukkel(szam):
    szamokneve = ["nulla","egy", "kettő", "három","négy","öt","hat","hét","nyolc","kilenc"]
    return szamokneve[szam]

for szam in range(10):
    print(szam,betukkel(szam))