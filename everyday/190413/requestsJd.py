# 百度
import requests

#获得一个网页最简单的一行代码
#通过给定get方法和url来构造一个向服务器请求资源的Request对象，这个对象是Request库内部生产的
#返回的内容用一个变量r来表示，r是一个esponse对象，response对象包含从服务器返回的所有的相关资源
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

#http://www.python-requests.org