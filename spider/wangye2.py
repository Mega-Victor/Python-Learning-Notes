# 获取二级网址
import requests
from bs4 import BeautifulSoup
import re
requests = requests.get(url='http://news.qq.com/world_index.shtml')
BeautifulSoup = BeautifulSoup(requests.text,'lxml')
f=open('D:\\桌面\\news.txt','w')
f.seek(0)

f.write('2017/02/07 tecent news\n')
# 利用正则获取所有新闻的url
news = BeautifulSoup.find_all('a',href = re.compile('http://news.qq.com/a/20170320/'))

for i in news:
    txt = i.text.strip() #strip() 用于去掉str的前后空格
    if txt == '':
        continue
    else:
        list = [txt,'url = ',i.attrs['href'],'\n']
        f.writelines(list)

f.close()