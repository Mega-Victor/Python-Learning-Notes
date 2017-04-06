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
        'Cookie': 'pac_uid=1_807387853; tvfe_boss_uuid=3403ff60466a623b; sd_userid=42081487762143688; sd_cookie_crttime=1487762143688; ptui_loginuin=807387853; uid_uin=144115199868538691; uid_a2=39e50b3287c31cd34fc4831ab7bde738ea075731cfee53d658cb7faf25ce083ab3d10ca5e4cce9578a310dc59f0d858813cf01b5ec249332f7cbfd9ce4450aebf92fbc357956a552; uid_type=2; uid_appid=1400000008; openid=o1a7pssL8vCDv5DPcNyShRa1XOvw; RK=4XMaLo7qVy; pt2gguin=o0807387853; uin=o0807387853; skey=@IM3HfDWUs; ptisp=edu; ptcz=eee75d95ec5af8b944a8a38ac707380dd4c3b0005bbe46dbbffe48224f18f655; mobileUV=1_15ad70ce593_e54ff; gj_mpvid=56252108; ptag=www_qq_com|/; ts_refer=www.qq.com/; main_login=wx; vuserid=144115199868538691; ad_play_index=41; pgv_info=ssid=s5275098712; ts_last=news.qq.com/world_index.shtml; pgv_pvid=2274749388; o_cookie=807387853; ts_uid=1417647856',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
    }
    web_s = 'http://news.qq.com/a/20170321'

    m = []
    for i in url_analysis(web_u, web_h, web_s):
        m.append(content(i, web_h))
    result = dict(m)
    write_txt('news.txt', 'D:\\桌面', result)
