from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.jackpincombe.online")
bsObj = BeautifulSoup(html.read())

print(bsObj.h1)

