# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
from itemadapter import ItemAdapter
import json


class IpPoolPipeline:
    # def __init__(self):

    # self.file = open("movie.txt","wb")
    fp = None

    def open_spider(self, spider):
        self.fp = open("diamzi.txt", "w", encoding="utf-8")

    def close_spider(self, spider):
        self.fp.close()

    def process_item(self, item, spider):
        self.fp.write(str(item) + "\n")
        return item


# 将数据存储到MySQL当中
class MysqlPipeline():
    conn = None

    def open_spider(self, spider):
        self.conn = pymysql.Connect(host="rm-wz9325c14dsxj3l0kko.mysql.rds.aliyuncs.com", port=3306, user="root",
                                    passwd="AZFZhh@H55XAuMu", db="project")
        print(self.conn)

    def process_item(self, item, spider):
        self.cursor = self.conn.cursor()
        sql = 'insert into duanziwang values("{}","{}")'.format(item["title"], item["content"])
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_psider(self, spider):
        self.cursor.close()
        self.conn.close()
