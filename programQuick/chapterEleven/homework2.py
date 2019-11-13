'''
1、从图像网站下载
编写一个程序，访问图像共享网站，如 Flickr 或 Imgur，查找一个类型的照片，
然后下载所有查询结果的图像。可以编写一个程序，访问任何具有查找功能的图像网站。
'''
# -*-coding:utf-8-*-
import os
import requests
import bs4

baseUrl = 'http://imgur.com'
dirName = 'image'
os.makedirs(dirName, exist_ok=True)
# 搜索参数
url = baseUrl + '/search/score?q=' + 'movie'
response = requests.get(url)
response.raise_for_status()
soup = bs4.BeautifulSoup(response.text, "html.parser")
imageUrls = soup.select(".image-list-link img")
if not imageUrls:
    print('Could not find image.')
else:
    for imageUrl in imageUrls:
        downloadUrl = imageUrl.get('src')
        print("Download image %s..." % downloadUrl)
        split = downloadUrl.split('/')
        fileName = os.path.basename(split[len(split) - 1])
        filePath = os.path.join(dirName, fileName)
        print("FilePath is  %s..." % filePath)
        if not os.path.exists(filePath):
            imageStream = requests.get('http:' + downloadUrl)
            imageStream.raise_for_status()
            imageFile = open(filePath, 'wb')
            for chunk in imageStream.iter_content(100000):
                imageFile.write(chunk)
