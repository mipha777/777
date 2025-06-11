import scrapy
from ..items import mySpider_01Item


class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250?start={}&filter="]
    page_num = 0

    def parse(self, response):
        # 这里获取了所有电影的名字、链接、评分
        # all_movies = response.xpath('')
        movieNames = response.xpath('//div[@class="article"]//li//a/span[@class="title"][1]/text()').getall()
        movielinks = response.xpath('//div[@class="article"]//li//a/@href').getall()
        moviestars = response.xpath('//div[@class="article"]//span[@class="rating_num"]/text()').getall()
        # 实例化一个item类 用以保存电影详细信息
        item = mySpider_01Item()
        # 循环遍历取出获取的电影信息
        for a, b, c in zip(movieNames, movielinks, moviestars):
            # 将取出的电影信息输入到item字典里面
            item['moviename'] = a
            item['movielink'] = b
            item['moviestar'] = c
            # print(item)
            yield item
        # 改变页码 获取下一页的电影信息内容
            if self.page_num < 50:
                self.page_num += 25
                url = "https://movie.douban.com/top250?start={}&filter=".format(str(self.page_num))
                # 回调函数
                yield scrapy.Request(url=url, callback=self.parse)

