import requests

kittens = requests.get("http://placekitten.com/")

#print(kittens.text[559:1000])

body = {'Name':'Eric', 'Age':'26'}

response = requests.post("http://placekitten.com")

print(response.status_code)