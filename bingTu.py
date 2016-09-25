#-*- coding:utf-8 -*-

import os
import requests
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup as bs

url = 'http://cn.bing.com'

headers = {'Referer': 'http://cn.bing.com',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36'
          }

try:
    r = requests.get(url, headers=headers)
except Exception as e:
    print u'出现个异常了，快找你男朋友解决。', e
    
html = r.text

url_pre = html.find('g_img={url:')

url_start = html.find('http', url_pre)
url_end = html.find('"', url_start)
url = html[url_start: url_end]
img_format = url[-4:]
print u'已找到图片'

bsObj = bs(html, 'html.parser')
a_tag = bsObj.find('a', {'id': "sh_cp"})
alt = a_tag.attrs['alt']

title = alt.split()[0]
##print(alt)

today = datetime.today().strftime('%Y%m%d')

try:
    if not os.path.exists('F://Bing_image'):
        os.mkdir('F://Bing_image')
    print u'正在下载'
    i = requests.get(url, headers=headers)
    img_name = today + ' - ' + title + img_format
    with open('F://Bing_image/' + img_name, 'wb') as f:
        f.write(i.content)
    print u'图片已保存在F盘的Bing_image目录下，名字是：%s' % img_name
    sleep(2)
except Exception as e:
    print u'出现个异常了，快找你男朋友解决。', e
