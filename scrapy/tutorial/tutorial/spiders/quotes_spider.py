import scrapy
# -*- coding: utf-8 -*-

'''class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
'''
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        baseurl = 'http://www.cctv-axsq.cn/a/xinwendongtai/list_18_'
        urls = []
        for i in range(1,20):
            urls.append(baseurl+str(i)+'.html')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    '''def parse(self, response):
        page = response.url[-6]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)'''

    def parse(self, response):
        #page = response.url[-6]
        filename = 'content.txt'
        with open(filename, 'a') as f:
            #f.write(response.body)
            for i in range(len(response.css("div.new_content"))):
                title='Title:'+response.css("p.new_title")[i].css("p::text").extract_first()+'\n'
                content='Content:'+response.css("div.new_content")[i].css("div::text").extract_first()+'\n\n'
                f.write(title)
                f.write(content)

