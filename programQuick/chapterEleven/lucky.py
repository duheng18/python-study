'''
从命令行参数中获取查询关键字。
取得查询结果页面。
为每个结果打开一个浏览器选项卡。
这意味着代码需要完成以下工作:
    从 sys.argv 中读取命令行参数。
    用 requests 模块取得查询结果页面。
    找到每个查询结果的链接。
    调用 webbrowser.open()函数打开 Web 浏览器。
    打开一个新的文件编辑器窗口，并保存为 lucky.py。
'''

# 获取命令行参数，并请求查找页面

import requests, sys, webbrowser, bs4

print('Googling...')  # display text while downloading the Google page
res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

# Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    webbrowser.open('http://www.baidu.com' + linkElems[i].get('href'))
