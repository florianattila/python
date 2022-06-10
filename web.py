import urllib.request
import sys

def download_function(url):
    try:
        content = urllib.request.urlopen(url)
        page_content = content.read()
        file = open(page_content)
        file.write(page_content)
        file.close()
        print("A tartalom letöltése folyamatban")
    except:
        print("A tartalom letöltése nem sikerült")

url = input("Kérem adja meg a webhely url-jét")
download_function(url)