# -*- coding:utf-8 -*-
# 京东
import requests

url = "https://item.jd.com/8735304.html"
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")