import sys 
oldout = sys.stdout
print("Képernyőre ír")
wr = open("test3.txt", "w")
sys.stdout = wr
print("Fájlba ír.")
wr.close()
print("Hová ír?")
sys.stdout = oldout