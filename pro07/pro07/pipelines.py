# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 在一个爬虫项目中我们最后编写的一部分是pipelines.py


class Pro07Pipeline(object):
    def process_item(self, item, spider):
        for i in range(0, len(item["content"])):
            print(item["content"][i])
            print(item["link"][i])
        return item
