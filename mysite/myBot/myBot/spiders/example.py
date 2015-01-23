# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from myBot.items import MovieItem


class ExampleSpider(BaseSpider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
    )

    def parse(self, response):
        return MovieItem(name='The Endless Journey')
