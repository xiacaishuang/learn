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
    start_urls = ['http://www.cctv-axsq.cn/a/xinwendongtai/',]
    def parse(self, response):
        filename = 'content.txt'
        with open(filename, 'a') as f:
            for i in range(len(response.css("div.new_content"))):
                title = 'Title:' + response.css("p.new_title")[i].css("p::text").extract_first() + '\n'
                content = 'Content:' + response.css("div.new_content")[i].css("div::text").extract_first() + '\n\n'
                f.write(title)
                f.write(content)
        if('下一页' in response.css('div.pages a::text').extract()):
            next_page = response.css('div.pages a::attr(href)')[-2].extract()
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)




