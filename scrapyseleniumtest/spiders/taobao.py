# -*- coding: utf-8 -*-
import scrapy


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['wwww.taobao.com']
    start_urls = ['http://wwww.taobao.com/']

    def parse(self, response):
        pass
