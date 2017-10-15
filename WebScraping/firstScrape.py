from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

'''
Using a try statement to ensure that if the script runs into any issues
the script will not crash but it will continue and will only throw an exception
'''

try:
    html = urlopen("http://www.jackpincombe.online")
    bsObj = BeautifulSoup(html.read())
    print(bsObj.h1)
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)

else:
    print("It worked")