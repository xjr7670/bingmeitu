#-*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs

url = 'http://cn.bing.com'

r = requests.get(url)
html = r.text

url_pre = html.find('g_img={url:') + 13
url_end = html.find('.jpg', url_pre) + 4
url = html[url_pre: url_end]
##print(url)

bsObj = bs(html, 'html.parser')
a_tag = bsObj.find('a', {'id': "sh_cp"})
alt = a_tag.attrs['alt']
title = alt.split()[0]
##print(alt)

i = requests.get(url)
with open(title + '.jpg', 'wb') as f:
    f.write(i.content)
