# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from twisted.enterprise import adbapi

import settings


class DemospiderPipeline(object):
    def process_item(self, item, spider):
        return item


class HuanQiuPipeline(object):

    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            sql = '''insert into scrapy.huanqiu_web (title,summary,source_url,source_name,display_time,cover_url) values (\'%s\',\'%s\',\'%s\',\'%s\',\'%s\',\'%s\')''' %(
                item['title'],item['summary'], item['source_url'], item['source_name'], item['display_date'],
                item['cover_url'])
            self.cursor.execute(sql)
            self.connect.commit();
        except Exception as e:
            print('err:', e)

    def close_spider(self, spider):
        self.connect.close()
