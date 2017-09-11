from scrapy.spider import Spider  
from scrapy.selector import Selector  

from tutorial.items import DmozItem  

class DmozSpider(Spider):  
    name = "dmoz"
    allowed_domains = ["hxdengberkeleyapp.herokuapp.com/"]  
    start_urls = [
    	"https://hxdengberkeleyapp.herokuapp.com/"
    ]

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//body')
        items = []
        for site in sites:  
            item = DmozItem()
            item['content'] = site.xpath('//body/h1/text()').extract()
            items.append(item)
        return items
