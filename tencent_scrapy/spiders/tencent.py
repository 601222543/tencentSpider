# -*- coding: utf-8 -*-
import sys
import scrapy
# 从items文件中导入类
from tencent_scrapy.items import TencentScrapyItem
from bs4 import BeautifulSoup

# # 设置python解释器默认编码
# reload(sys)
# sys.setdefaultencoding("utf-8")

class TencentSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]

    main_url = "http://hr.tencent.com/position.php?&start=%d"
    page = 0
    start_urls = [main_url + str(page)]

    def parse(self, response):
        for each in response.xpath('//tr[@class="even"] | //tr[@class="odd"]'):
            # 实例化一个items,每一页都需要一个items,所以在循环内
            item = TencentScrapyItem()
            # 职位名
            item['positionName'] = each.xpath('./td[1]/a/text()').extract()[0]
            # 详细链接
            item['positionLink'] = "http://hr.tencent.com/" + each.xpath('./td[1]/a/@href').extract()[0]
            # 职位类别
            item['positionType'] = each.xpath('./td[2]/text()').extract()[0]
            # 招聘人数
            item['popNum'] = each.xpath('./td[3]/text()').extract()[0]
            # 工作地点
            item['workLocation'] = each.xpath('./td[4]/text()').extract()[0]
            # 发布时间
            item['publishTime'] = each.xpath('./td[5]/text()').extract()[0]

            yield item
            # yield scrapy.Request(item['positionLink'], callback=self.parse)

        if self.page <= 2280:
            # 重新发下一个链接的请求
            self.page += 10
        # 两个参数,请求的url,和等待处理相应的回调函数
        yield scrapy.Request(self.main_url + str(self.page), callback=self.parse)

    # def detailInfo(self, response):
    #     print "="*100
    #     body = response.body
    #     soup = BeautifulSoup(body, "html5lib")
    #
    #     for each in soup.find_all("ul", {"class": "squareli"}):
    #         print each.li.string






