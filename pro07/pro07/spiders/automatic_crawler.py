# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from pro07.items import Pro07Item

# 这是一个爬取全站信息的自动网络爬虫


class AutomaticCrawlerSpider(CrawlSpider):
    name = 'automatic_crawler'
    allowed_domains = ['qiushibaike.com']

    def start_requests(self):
        ua = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko'}
        yield Request('http://www.qiushibaike.com/', headers=ua)

    rules = (
        # 设置url链接的提取规则
        Rule(LinkExtractor(allow='article'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = Pro07Item()
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()

        # 将提取的内容保存到item对象的content容器中
        i["content"] = response.xpath("//div[@class='content']/text()").extract()
        # 将提取的url保存到item对象的link容器中
        i["link"] = response.xpath("//link[@rel='canonical']/@href").extract()

        # 也可以最后在pipelines.py中输出
        print(i["content"])
        print(i["link"])
        return i
