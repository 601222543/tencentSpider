# -*- coding: utf-8 -*-
import scrapy

class TencentScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位名
    positionName = scrapy.Field()
    # 详细链接
    positionLink = scrapy.Field()
    # 职位类别
    positionType = scrapy.Field()
    # 招聘人数
    popNum = scrapy.Field()
    # 工作地点
    workLocation = scrapy.Field()
    # 发布时间
    publishTime = scrapy.Field()





