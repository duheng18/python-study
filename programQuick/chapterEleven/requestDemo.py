import requests

res=requests.get('http://www.baidu.com')
print(type(res))
print(res.status_code)
print(requests.codes.ok)
print(len(res.text))
print(res.text[:100])
print(res.raise_for_status())
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s'%(exc))