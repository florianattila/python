import sys
oldout = sys.stdout
print("képernyőre ír")
wr = open("test2.txt", "w")
sys.stdout= wr
print("Fájlba írás")
wr.close()
sys.stdout = oldout
print("Képernyőre ír ismét")