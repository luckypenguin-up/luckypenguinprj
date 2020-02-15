#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib.request


# 通过url获取网页
def getHtml(url: object) -> object:
    # 要设置请求头，让服务器知道不是机器人
    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0')
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


# 通过正则表达式来获取图片地址，并下载到本地
def getImg(html):
    reg = r'src="(https.+?\)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    x = 0
    for imgurl in imglist:
        print(imgurl)
        # 通过urlretrieve函数把数据下载到本地的D:\\images，所以你需要创建目录
        urllib.urlretrieve(imgurl, '/Users/liqian/test1/%s.jpg' % x)
        x = x + 1


html = getHtml("http://www.qiushibaike.com/imgrank/")
getImg(html)
