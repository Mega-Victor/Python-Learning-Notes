import requests
from bs4 import BeautifulSoup
import re


def url_analysis(u, h, s, n):
    '''
    用于分析网页,得到一个含有二级网址的标签列表
    :param u: 起始网址
    :param h: 头部信息
    :param s: 二级网址包含的特定字段
    :param n:页码
    :return:
    '''
    url_lst = []
    for i in range(1, n + 1):
        r = requests.get(url=u + str(i) + '/', headers=h)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        r2 = soup.find_all('a', href=re.compile(s))
        for j in r2[::2]:
            r3 = j.attrs['href']
            url_lst.append(r3)
    return (url_lst)


def content(u, h):
    '''
    爬取网页标签信息
    :param u: 二级网址
    :param h: 头部信息
    :return:
    '''
    r = requests.get(url=u, headers=h)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    t = soup.title.text  # 爬取标题
    # 总价
    totalprice = soup.find('div', class_="price").find('span', class_="mainInfo bold").text
    # 房间数量
    introductionList = soup.find('div', class_="base").find('div', class_="content").find_all('li')
    roomifo = introductionList[0].text
    # 总面积
    area = soup.find('div', class_="area").find('div', class_="mainInfo").text

    tableinfo = soup.find('table', class_="aroundInfo hideAnswerFast").find_all('tr').find('span',class_='title')
    # 单价
    unitprice=tableinfo[0].text
    # 装修
    decration = tableinfo[3].text
    # 首付
    firstprice = tableinfo[5].text
    # 月供
    monthprice = tableinfo[6].text
    # base = soup.find('div', class_="base").find('div', class_="content").find_all('li')
    # year = base[-1].text[-3:-1]
    # pattern = 'resblockPosition:\'(.*?)\,\n'
    # position = re.search(pattern, r.text).group(1)
    # lng = position.split(',')[0]
    # lat = position.split(',')[1]
    return ([t, ',', totalprice, ',', roomifo, ',', area, ',', unitprice, ',', decration, ',', firstprice, ',', monthprice, ',', lng, ',''\n'])


if __name__ == '__main__':  # main 函数
    web_u = 'http://su.lianjia.com/ershoufang/d'
    web_h = {'Accept-Language': 'zh-CN,zh;q=0.8',
             'Upgrade-Insecure-Requests': '1',
             'Connection': 'keep-alive',
             'Host': 'su.lianjia.com',
             'Cookie': 'iknew_callEsay=true; lianjia_uuid=2170f3d9-a9d6-445d-84b3-fd53bdf619ea; _ga=GA1.2.178358532.1483019972; _smt_uid=586515a1.96682e2; select_city=320500; cityCode=su; ubt_load_interval_b=1490358564312; ubt_load_interval_c=1490358564312; ubta=1641808036.961307658.1483019972458.1490358507831.1490358565366.64; ubtb=1641808036.961307658.1490358565371.40BCFF6C4A2B10A46E24CEC8F0624B87; ubtc=1641808036.961307658.1490358565371.40BCFF6C4A2B10A46E24CEC8F0624B87; ubtd=41',
             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36', 'Accept-Encoding': 'gzip, deflate, sdch'}

    web_s = 'http://su.lianjia.com/ershoufang/su4430847.html'

    f = open('D:\\桌面\\tes.csv', 'w')
    f.seek(0)
    # f.write('title,total_price万元,unitprice元/平方米,area平方米,产权年限,lng,lat')
    for i in url_analysis(web_u, web_h, web_s, 1):
        data = content(i, web_h)
        f.writelines(data)
    f.close()
    print('finish')
