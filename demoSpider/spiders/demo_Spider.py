import scrapy as scrapy
import json

from demoSpider.items import HuanQiuItem


class demo_Spider(scrapy.Spider):
    name = 'demo_Spider1'
    allowed_domains = ['china.huanqiu.com']
    start_urls = ['https://china.huanqiu.com/api/list2?node=/e3pmh1nnq/e7tl4e309&offset=0&limit=25']

    # 自定义配置文件
    custom_settings = {

        # 指定管道缓存最多数据条数
        'ITEM_PIPELINES': {
            'demoSpider.pipelines.HuanQiuPipeline': 300,
        }
    }

    # no.1 解析api接口，返回json数据

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse_detail, method='GET', headers=None,
                             errback=None)

    def parse(self, response):
        pass

    def parse_detail(self, response: scrapy.http.Response):
        news_data_list = response.text
        json_news = json.loads(news_data_list)

        for i in json_news['list']:
            item = HuanQiuItem()
            item['title'] = i['title']
            item['summary'] = i['summary']
            item['source_url'] = i['source']['url']
            item['source_name'] = i['source']['name']
            item['display_date'] = i['ext_displaytime']
            item['cover_url'] = i['cover']
            yield item
