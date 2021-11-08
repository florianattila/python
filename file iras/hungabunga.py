forrasfajl = open("raspberries.txt", "w")
rpik = []
for sor in forrasfajl:
    rpik.append(sor.strip().split(";"))
forrasfajl.close()