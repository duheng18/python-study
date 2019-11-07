'''
下面是程序要做的事:
加载主页;
保存该页的漫画图片;
转入前一张漫画的链接;
重复直到第一张漫画。

这意味着代码需要做下列事情:
• 利用 requests 模块下载页面。
• 利用 Beautiful Soup 找到页面中漫画图像的 URL。
• 利用 iter_content()下载漫画图像，并保存到硬盘。
• 找到前一张漫画的链接 URL，然后重复。
打开一个新的文件编辑器窗口，将它保存为 downloadXkcd.py。
'''
'''
  打开一个浏览器的开发者工具，检查该页面上的元素，你会发现下面的内容:
• 漫画图像文件的 URL，由一个<img>元素的 href 属性给出。
• <img>元素在<div id="comic">元素之内。
• Prev 按钮有一个 rel HTML 属性，值是 prev。
• 第一张漫画的 Prev 按钮链接到 http://xkcd.com/# URL，表明没有前一个页面了。
'''
import requests, os, bs4

url = 'http://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s ...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    print('comicElem:', comicElem)
    print(len(comicElem))
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'http:' + comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

        # Save the image to ./xkcd.
        imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Pre button's url.
    preLink = soup.select('a[rel="prev"]')[0]
    print('preLink:', preLink)
    url = 'http://xkcd.com' + preLink.get('href')
print('Done.')
