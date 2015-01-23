# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from myBot.items import MovieItem


class ExampleSpider(BaseSpider):
    name = "example"
    start_urls = (
        'http://www.imdb.com/chart/top?ref_=nv_ch_250/',
    )

    def parse(self, response):
        title = response.xpath('//title')
        return MovieItem(name=title)
