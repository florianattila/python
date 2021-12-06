#Rendezzünk egy szöveges adatokat tartalmazó listát!
szoveg_lista = ["barack", "alma", "mandarin"]
szoveg_lista.sort()
print(szoveg_lista)
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort()
print(szoveg_lista2)
# a nyelv és a kódolás beállítása
import locale
import functools
locale.setlocale(locale.LC_ALL, "HU_hu.UTF8") 
szoveg_lista2 = ["én", "te", "ő", "mi", "ti", 'ők']
szoveg_lista2.sort(key = functools.cmp_to_key(locale.strcoll))
print(szoveg_lista2)