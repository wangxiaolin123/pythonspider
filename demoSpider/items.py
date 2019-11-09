# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class HuanQiuItem(scrapy.Item):
    title = scrapy.Field()  # 标题
    summary = scrapy.Field()  # 关键词
    source_url = scrapy.Field()  # 新闻详细url
    source_name = scrapy.Field()  # 来源网站
    display_date = scrapy.Field()  # 新闻发布时间
    cover_url = scrapy.Field()  # 新闻封面
