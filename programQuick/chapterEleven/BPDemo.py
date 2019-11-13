import requests, bs4

res = requests.get('http://www.baidu.com')
print(res.raise_for_status())
bdSoup = bs4.BeautifulSoup(res.text)
print(type(bdSoup))

exampleFile=open('example.html')
exampleSoup=bs4.BeautifulSoup(exampleFile)
print(type(exampleSoup))
