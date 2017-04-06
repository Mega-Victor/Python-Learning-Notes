import requests
from bs4 import BeautifulSoup

requests = requests.get(url='http://news.qq.com/a/20170320/024127.htm')
headers = requests.headers

BeautifulSoup = BeautifulSoup(requests.text,'lxml')
title = BeautifulSoup.title.text

f= open('D:\\桌面/test.txt','w')
f.seek(0)

f.write('lianjie : http://news.qq.com/a/20170320/024127.htm\n')
f.write('title : '+title+'\n')
for i in headers:
    list=[i,' : ',headers[i]+'\n']
    print(list)
    f.writelines(list)
f.close()






