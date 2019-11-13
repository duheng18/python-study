'''
11.11.4 链接验证
编写一个程序,对给定的网页URL,下载该页面所有链接的页面。程序应该标记出所有具有
404“Not Found”状态码的页面，将它们作为坏链接输出。'''

# -*-coding:utf-8-*-
import requests
import bs4

url = 'http://ifeve.com/'
response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, "html.parser")
a_list = soup.select('a')
for a in a_list:
    a_url = a.get('href')
    try:
        response = requests.get(a_url)
        if response.status_code == requests.codes.not_found:
            print("Page %s is broken link" % a_url)
        else:
            print("Page %s is other type link" % a_url)
        response.raise_for_status()
    except:
        print("Page %s is Error" % a_url)