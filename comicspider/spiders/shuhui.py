from scrapy.selector import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from comicspider.items import ComicspiderItem
from bs4 import BeautifulSoup
import datetime
import re

class ShuhuiSpider(CrawlSpider):
    name = 'shuhui'
    allowed_domains = ['ishuhui.com']
    start_urls = ['http://ishuhui.com']

    #define the rules
    rules = (
        Rule(SgmlLinkExtractor(allow=('archives.\d+')), callback='parse_episode'),
    )

    # def parse(self, response):
    #     sel = Selector(response)
    #     i = ComicspiderItem()

    #     filename = response.url.split("/")[-2]
    #     open(filename, 'wb').write(response.body)

    #     #grabbing the data
    #     #i['domain_id'] = sel.xpath('//input[@id="sid"]/@value').extract()
    #     #i['name'] = sel.xpath('//div[@id="name"]').extract()
    #     #i['description'] = sel.xpath('//div[@id="description"]').extract()
    #     return i
    def parse_episode(self, response): 

        item = ComicspiderItem()

        soup = BeautifulSoup(response.body)
        soup.prettify()
        items = []
        image_links = []
        
        item['link'] = response.url
        
        #getting the title 
        divs = soup.findAll('h1')
        title = divs[0].string.strip()

        #getting the episode number
        item['episode_number'] = re.search(r'\d+', title).group()
        item['title'] = title

        #getting the web pages
        episode = soup.find('div', class_="article-content")
        pages = episode.find_all('img')
        for page in pages:
            self.log("The image url is %s" % page['src'])
            image_links.append(page['src'])

        # add this later
        item['image_urls'] = image_links
        item['category'] = 'comic'
        item['post_type'] = 'comic'
        item['soft_delete'] = 0
        item['created_at'] = datetime.datetime.utcnow()

        items.append(item)
        
        return items

