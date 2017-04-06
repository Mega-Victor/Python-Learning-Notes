# 获取二级网址下的内容
import requests
from bs4 import BeautifulSoup
import re
r = requests.get(url='http://mil.qq.com/mil_index.htm')
soup = BeautifulSoup(r.text,'lxml')
f=open('D:\\桌面\\news.txt','w',encoding='utf-8')
f.seek(0)

f.write('2017/02/07 tecent news\n')
# 利用正则获取所有新闻的url
news =soup.find_all('a',href = re.compile('http://mil.qq.com/a/20170320'))

for i in news:
    txt = i.text.strip() #strip() 用于去掉str的前后空格
    if txt == '':
        continue
    else:
        u = i.attrs['href']
        ur = requests.get(url=u)
        usoup = BeautifulSoup(ur.text,'lxml')
        f.write(txt+'\n')
        f.write('正文如下:\n')
        # print(u)
        # print(usoup.body.attrs)
        if usoup.body.attrs['id'] == 'P-QQ':
            continue
        else:
            p = usoup.find('div',id="Cnt-Main-Article-QQ").find_all('p')
            for i in p:
                f.write(i.text +'\n')
    f.write('\n')
f.close()
print('finished')