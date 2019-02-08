import scrapy

class MainSpider(scrapy.Spider):
    name = "nykaa"
    def start_requests(self):
        urls = ['https://www.nykaa.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'nykaa-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)                
