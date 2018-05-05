#!/usr/bin/python
#-*- coding:utf-8 _*-  
# #  FileName    : get_book
# #  Author      : XiaoHua Wen <wenhua.maker@gmail.com>
# #  Created     : 2018/1/26
# #  Copyright   : 2018-2020
# #  Description :

import requests
import time
from lxml import etree
from fake_useragent import UserAgent
def get_header():
    ua = UserAgent().random
    headers = {
        'User-Agent': ua,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate',
    }
    return headers
def contant():
    url = 'https://www.ebooksplan.club/%E5%85%A8%E9%83%A8%E8%B5%84%E6%BA%90/'
    headers = get_header()
    response = requests.get(url,headers=headers).text
    selector=etree.HTML(response)
    content=selector.xpath('//td[@class="fb-n"]/a/text()')[1:]
    content_url = selector.xpath('//td[@class="fb-n"]/a/@href')[1:]
    for i,href in enumerate(content_url,0):
        content_url[i] = 'https://www.ebooksplan.club'+href
    return ','.join(content),content_url

def books(urls):
    book_list = []
    url_list =[]
    for url in urls:
        time.sleep(3)
        headers = get_header()
        response = requests.get(url,headers=headers).text
        selector=etree.HTML(response)
        content=selector.xpath('//td[@class="fb-n"]/a/text()')
        content_url = selector.xpath('//td[@class="fb-n"]/a/@href')[1:]
        for i, href in enumerate(content_url, 0):
            content_url[i] = 'https://www.ebooksplan.club' + href
        book_list += content
        url_list += content_url

    return book_list,url_list

if __name__ == '__main__':
    print(books(contant()[1]))

