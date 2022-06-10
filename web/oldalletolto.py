import urllib.request
import sys

def download_function(url):
    try:
        content = urllib.request.urlopen(url)
        page_content = content.read()
        file = open("page_content.txt", "wb")
        file.write(page_content)
        file.close()
        print("Content downloaded successfully")
    except:
        print("Something went wrong")

url = input("Please insert an url")
download_function(url)