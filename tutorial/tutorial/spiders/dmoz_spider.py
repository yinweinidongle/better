from scrapy.spider import Spider
from scrapy.selector import Selector
from tutorial.items import DmozItem
class DmozSpider(Spider):
   name = "dmoz"
   allowed_domains = ["dmoz.org"]
   start_urls = [
	   "http://t3.9laik.info/pw/htm_data/14/1702/550598.html",
   
   ]
   
   def parse(self, response):
	   sel = Selector(response)
	   sites = sel.xpath('//div')
	   items = []
	   for site in sites:
		   item = DmozItem()
		   item['title'] = site.xpath('img/@src').extract()
		 
		   items.append(item)
	   return items