import scrapy
# 导入Pro07Item类, 为了使用items.py中定义的容器
from pro07.items import Pro07Item

# 这是一个非自动网络爬虫


class Scrapy01Spider(scrapy.Spider):
    name = "scrapy01"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com',
    )

    # 爬取获得的信息存储在response中
    def parse(self, response):
        # 创建Pro07Item类的对象
        item = Pro07Item()
        # 将提取的内容保存到item对象的content容器中
        item["content"] = response.xpath("/html/head/title/text()").extract()
        # 用yield返回结果到pipelines.py中
        yield item
