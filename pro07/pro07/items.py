# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# 要使用scrapy框架必须先导入scrapy包
import scrapy

# 在一个爬虫项目中我们最先编写的部分是items.py


class Pro07Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 创建一些容器, 容器使用前必须先在items.py中创建.
    content = scrapy.Field()
    link = scrapy.Field()
