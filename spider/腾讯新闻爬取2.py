import requests
from bs4 import BeautifulSoup
import re


def url_analysis(u, h, s):
    '''
    用于分析网页,得到一个含有二级网址的标签列表
    :param u: 起始网址
    :param h: 头部信息
    :param s: 二级网址包含的特定字段
    :return:
    '''
    r = requests.get(url=u, headers=h)
    soup = BeautifulSoup(r.text, 'lxml')
    # 找到所有的二级网址
    news = soup.find_all('a', href=re.compile(s), class_='linkto')
    return (news)


def content(new, h):
    '''
    用于抓取网页中的标题以及新闻内容
    :param new: 含有二级网址链接的标签
    :param h: 头部信息
    :return:
    '''
    global p2
    t = new.text.strip()
    u2 = new.attrs['href']
    r2 = requests.get(url=u2, headers=h)
    soup2 = BeautifulSoup(r2.text, 'lxml')
    if soup2.body.attrs['id'] != "P-QQ":
        p = soup2.find('div', id="Cnt-Main-Article-QQ").find_all('p')
        p_lst = []
        for i in p:
            p_lst.append(i.text)
        p2 = '\n'.join(p_lst)
    return ([t, p2])


def write_txt(name, path, content_dict):
    '''
    用于把爬取的数据写入文档txt
    :param name: 新建文档的名字
    :param path: 路径
    :param content_dict: 需要写入的数据
    :return:
    '''
    f = open(path + '\\' + name, 'w', encoding='utf-8')
    f.seek(0)
    f.write('腾讯新闻\n\n\n')
    for i in content_dict:
        f.write(i + '\n')
        f.write(content_dict[i])
        f.write('\n')
    f.close()


if __name__ == '__main__':  # main 函数
    web_u = 'http://news.qq.com/world_index.shtml'
    web_h = {
        'Referer': 'http',
        'Upgrade-Insecure-Requests': '1',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Host': 'news.qq.com',
        'Cookie':
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    web_s = 'http://news.qq.com/a/20170321'

    m = []
    for i in url_analysis(web_u, web_h, web_s):
        m.append(content(i, web_h))
    result = dict(m)
    write_txt('news.txt', 'D:\\桌面', result)
