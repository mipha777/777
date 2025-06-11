# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


import pymongo
from itemadapter import ItemAdapter


class MongoPipeline:
    # 所保存的数据库名称
    collection_name = "mydb"

    # mongodb初始化
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri  # 127.0.0.1
        self.mongo_db = mongo_db  # 数据库内表格名字

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"), # 数据库地址
            mongo_db=crawler.settings.get("MONGO_DATABASE", "items"), # 数据库名字
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item
