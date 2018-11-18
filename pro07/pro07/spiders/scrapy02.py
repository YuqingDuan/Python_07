# -*- coding: utf-8 -*-
import scrapy
# 导入Pro07Item类
from pro07.items import Pro07Item
# 进行浏览器伪装需要导入的包
from scrapy.http import Request

# 这是一个只爬取首页的自动网络爬虫


class Scrapy02Spider(scrapy.Spider):
    name = 'scrapy02'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['http://www.qiushibaike.com/']

    # 设计首次爬取的网页
    def start_requests(self):
        ua = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        yield Request('http://www.qiushibaike.com/', headers=ua)

    def parse(self, response):
        # 创建Pro07Item类的对象
        item = Pro07Item()
        # 将提取的内容保存到item对象的content容器中
        item["content"] = response.xpath("//div[@class='content']/span/text()").extract()
        # 将提取的url保存到item对象的link容器中
        item["link"] = response.xpath("//a[@class='contentHerf']/@href").extract()
        # 用yield返回结果到pipelines.py中
        yield item
