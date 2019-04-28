# -*- coding:utf-8 -*-
# 亚马逊
import requests

# r=requests.get("https://www.amazon.cn/gp/product/B07CKM9C75/")
# print(r.status_code)
# print(r.encoding)
# print(r.text)
# print(r.request.headers)
kv = {'user-agent': 'Mozilla/5.0'}
url = "https://www.amazon.cn/gp/product/B07CKM9C75/"
r = requests.get(url, headers=kv)
print(r.status_code)
print(r.request.headers)
print(r.text[:1000])
