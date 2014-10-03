import os
import random
from scrapy.conf import settings
import base64

class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers.setdefault('User-Agent', ua)

class ProxyMiddleware(object):
	def process_request(self, request, spider):
		request.meta['proxy'] = 'proxy.crawlera.com:8010'
		proxy_user_pass = "shakurapanda:CTgbPX3HAe"

		encode_user_pass = base64.encodestring(proxy_user_pass)
		request.headers['Proxy-Authorization'] = 'Basic ' + encode_user_pass
