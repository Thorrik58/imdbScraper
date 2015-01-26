# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from myBot.items import MovieItem


class example(BaseSpider):
    name = "example"
    allowed_domains = ["imdb.com"]
    start_urls = (
        'http://www.imdb.com/chart/top?ref_=nv_ch_250/',
    )

    def parse(self, response):
        for sel in response.xpath("//*[@class='chart']/tbody/tr/td[2]"):
            return MovieItem(name=sel.xpath('a/text()').extract()[0])