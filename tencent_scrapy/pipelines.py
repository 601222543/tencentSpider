# -*- coding: utf-8 -*-
import json

class TencentScrapyPipeline(object):
    def __init__(self):
        self.file = open('result.json', 'w')

    def process_item(self, item, spider):
        print type(item)
        text = json.dumps(dict(item), ensure_ascii=False) + "\n"
        print  "+"*20
        self.file.write(text.encode("utf-8"))
        return item

    def close_spider(self, spider):
        self.file.close()