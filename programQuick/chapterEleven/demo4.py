import requests, bs4

res = requests.get('https://nostarch.com/')
# print(res.raise_for_status())
# noStartSoup = bs4.BeautifulSoup(res.text)

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
# <class 'bs4.BeautifulSoup'>
print(type(exampleSoup))
