# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import pymysql
import scrapy
from itemadapter import ItemAdapter
import json
import requests


class IpPoolPipeline:
    # def __init__(self):

    # self.file = open("movie.txt","wb")
    fp = None

    def start_requests(self):
        urls = [
            "http://proxy.mimvp.com/exist.php",
            "https://proxy.mimvp.com/exist.php",
        ]
        for url in urls:
            meta_proxy = ""
            if url.startswith("http://"):
                meta_proxy = "http://180.96.27.12:88"  # http代理
            elif url.startswith("https://"):
                meta_proxy = "http://109.108.87.136:53281"  # https代理

            yield scrapy.Request(url=url, meta={'proxy': meta_proxy})

    def check_proxy(self,ip, port):
        """第二种："""
        try:
            # 设置重连次数
            requests.adapters.DEFAULT_RETRIES = 3
            # IP = random.choice(IPAgents)
            proxy = f"http://{ip}:{port}"
            # thisIP = "".join(IP.split(":")[0:1])
            # print(thisIP)
            res = scrapy.Request(url="http://icanhazip.com/", timeout=2, proxies={"http": proxy})
            proxyIP = res.text
            if (proxyIP == proxy):
                print("代理IP:'" + proxyIP + "'有效！")
                return True
            else:
                print("2代理IP无效！")
                return False
        except:
            print("1代理IP无效！")
            return False


    def process_item(self, item, spider):
        self.fp.write(str(item) + "\n")
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

        try:
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()

    def close_psider(self, spider):
        self.cursor.close()
        self.conn.close()
