# 百度
import requests

r = requests.get("http://www.baidu.com")
# r.status_code HTTP请求的返回状态，200表示连接成功，404表示失败
print(r.status_code)
# r.text HTTP响应内容的字符串形式，即URL对应的页面内容
print(r.text)
# r.encoding从HTTP header中猜测的响应内容编码方式
print(r.encoding)
# r.apparent_encoding从内容中分析出的响应内容编码方式（备选编码方式）
print(r.apparent_encoding)
# r.content响应内容的二进制形式
print(r.content)
# print(type(r))
# print(r.headers)
r.encoding='utf-8'
print(r.text)