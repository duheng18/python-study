# -*- coding:utf-8 -*-
import requests
url="http://m.ip138.com/ip.asp?ip="
try:
    r=requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.status_code)
    print(r.text[-500:])
except:
    print("抓取失败")