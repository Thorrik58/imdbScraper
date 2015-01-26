# -*- coding: utf-8 -*-
import scrapy
from scrapy.spider import BaseSpider
from myBot.items import MovieItem


class movieSpider(BaseSpider):
    name = "example"
    allowed_domains = ["imdb.com"]
    start_urls = (
        'http://www.imdb.com/chart/top?ref_=nv_ch_250/',
    )

    def parse(self, response):
        for sel in response.xpath("//*[@class='chart']/tbody/tr/td[@class='titleColumn']"):
            nam = sel.xpath('a/text()').extract()[0]
            rat = sel.xpath('span[@name="ir"]/@data-value').extract()[0]
            ran = sel.xpath('span[@name="ir"]/text()').re('\d+')[0]
            dat = sel.xpath('span[@name="rd"]/@data-value').extract()[0]
            yea = (sel.xpath('span[@name="rd"]/@data-value').extract()[0])[:4]
            MovieItem(name=nam,rating=rat,ranking=ran, pubdate=dat, year=yea).save()

            #print (sel.xpath('a/text()').extract()[0])
            #name (sel.xpath('a/text()').extract()[0])
            #rating (sel.xpath('span[@name="ir"]/@data-value').extract()[0])
            #year (sel.xpath('span[@name="rd"]/@data-value').extract()[0])
            #ranking (sel.xpath('span[@name="ir"]/text()').re('\d+')[0])
