from urllib.request import urlopen

html = urlopen("http://www.jackpincombe.online")
print(html.read())