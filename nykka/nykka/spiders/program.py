import scrapy, json, datetime

class MainSpider(scrapy.Spider):
    name = "nykaa"
    def start_requests(self):
        urls = ['https://www.nykaa.com/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        all_anchors= response.xpath("//a")
        mappingDict ={}
        for a in all_anchors:
            text= a.xpath("text()").extract_first()
            link = a.xpath("@href").extract_first()
            mappingDict[link]=text
            print(text, "---->",  link)  
        
        filename = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S") + 'nykaaMainPageLinks.txt'  
        with open(filename, "w") as file:
            file.write(json.dumps(mappingDict))                
