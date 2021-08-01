# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
import scrapy
from itemadapter import ItemAdapter

from concurrent.futures import ThreadPoolExecutor
import threading


class IpPoolPipeline:



    def process_item(self, item, spider):
        # print(item)
        return item


from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImagePipLine(ImagesPipeline):
    def get_media_requests(self, item, info):
        url = item["image_src"]
        print(url)
        yield scrapy.Request(url=url, meta={"item": item})

    def file_path(self, request, response=None, info=None, *, item=None):
        item = request.meta["item"]
        filePath = item["image_name"]
        print(filePath)
        return filePath

    def item_completed(self, results, item, info):
        return item


# 将数据存储到MySQL当中
class MysqlPipeline:
    conn = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="rm-wz9325c14dsxj3l0kko.mysql.rds.aliyuncs.com", port=3306, user="root",
                                    passwd="AZFZhh@H55XAuMu", db="project")

        print(self.conn)

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        sql = 'insert into ip_pool (address,type,platform) values("{}","{}","{}")'.format(
            item["ip"] + ":" + item["port"], item["type"], item["platform"])
        # print(sql)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_psider(self, spider):
        self.cursor.close()
        self.conn.close()
