# Scrapy settings for comicspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'comicspider'

SPIDER_MODULES = ['comicspider.spiders']
NEWSPIDER_MODULE = 'comicspider.spiders'

CRAWLERA_ENABLED = True
CRAWLERA_USER = 'shakurapanda'
CRAWLERA_PASS = 'CTgbPX3HAe'

AWS_ACCESS_KEY_ID = "AKIAJ73LZ7VPKF7DSI5Q"
AWS_SECRET_ACCESS_KEY = "GXnsMaSWebiVrmJORv9J/T0WHwLXRullPrwjnPTf"
IMAGES_STORE = "s3://enginehost.com/yuna/"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'comicspider (+http://www.yourdomain.com)'
# More comprehensive list can be found at 
# http://techpatterns.com/forums/about304.html
USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'
]

DOWNLOADER_MIDDLEWARES = {
         'comicspider.middlewares.RandomUserAgentMiddleware': 400,
         'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
         'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
         'scrapylib.crawlera.CrawleraMiddleware': 600
    # Disable compression middleware, so the actual HTML pages are cached
}

ITEM_PIPELINES = {
	'comicspider.pipelines.DuplicateTitlePipeline': 100,
	'comicspider.pipelines.CustomImagePipeline': 200,
	'comicspider.pipelines.DatabaseStoragePipline': 300
}