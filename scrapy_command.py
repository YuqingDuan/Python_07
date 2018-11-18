#查询scrapy中有哪些命令：scrapy -h
#命令分为：全局命令(不依赖于项目)，项目命令(依赖于项目)

import scrapy

#全局命令
    #查询fetch命令的使用方式：scrapy fetch -h
    scrapy fetch http://www.baidu.com --nolog

    #爬虫项目里面含有多个爬虫文件，之前用原始的urllib编写的是爬虫(文件)
    #运行测试单独的爬虫文件(不需要创建爬虫项目也不用进入爬虫项目目录)，先进入文件所在的文件夹的目录，再输入指令：
    scrapy runspider xxx.py

    #进入scrapy的交互终端
    scrapy shell http://www.baidu.com --nolog
    #离开scrapy的交互终端
    exit()

    #创建爬虫项目
    scrapy startproject xxx

    #查看scrapy框架版本
    scrapy version

    #下载某网页并在默认浏览器中查看
    scrapy view http://news.163.com




#项目命令
    #先cd到项目中
    #bench指令创建本地服务器(自动的)之后测试本地硬件的性能：1550 pages/min
    scrapy bench
    #爬虫项目的目录结构
    -project1
        -project1 爬虫项目核心目录
            -spiders 爬虫文件夹
            -__init__.py 爬虫项目初始化文件
            -items.py  爬虫项目目标文件，设定要爬取的内容
            -pipelines.py 信息的后续处理
            -settings.py 爬虫项目配置文件
        -scrapy.cfg 爬虫项目配置文件
    #查看爬虫模板 basic，crawl，csvfeed，xmlfeed
    scrapy genspider -l
    #创建爬虫文件 scrapy genspider -t 模板名 文件名 域名
    scrapy genspider -t basic weisuen baidu.com
    #测试创建的爬虫文件
    scrapy check weisuen
    #运行创建的爬虫文件
    scrapy crawl weisuen
    #展示当前可以使用的爬虫文件
    scrapy list
    #Linux中直接通过编辑器打开某个爬虫文件
    scrapy edit weisuen
    #没有爬虫的情况下用parse获取指定url并进行处理和分析，也可以指定爬虫去parse
    scrapy parse http://www.baidu.com
    











    
    


















