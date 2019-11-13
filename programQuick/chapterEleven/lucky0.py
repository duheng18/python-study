import requests, bs4, webbrowser, sys

print('Google...')
# 获取命令行参数，并请求查找页面
res = requests.get('http://google.com/search?q=' + ''.join(sys.argv[1:]))
res.raise_for_status()

# 找到所有结果
soup = bs4.BeautifulSoup(res.text)

linkElems = soup.select('.r a')

#  针对每个结果打开Web浏览器
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))
