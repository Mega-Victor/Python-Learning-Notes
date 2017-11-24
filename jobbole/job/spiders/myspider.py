import scrapy
from job.items import StackItem

class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["mportnew.com"]
    start_urls = [
        "http://www.importnew.com/all-posts/page/%d"%d for d in range(122)
    ]
    # Scrapy为Spider的 start_urls 属性中的每个URL创建了 scrapy.Request 对象，
    # 并将 parse 方法作为回调函数(callback)赋值给了Request。
    # Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。
    def parse(self, response):
        t = response.xpath('//div[@class ="post-meta"]/p[1]')
        for i in t:
            item = StackItem()
            item['title'] = i.xpath('a[@class="meta-title"]/@title').extract()
            item['url'] = i.xpath('a[@class="meta-title"]/@href').extract()
            yield item