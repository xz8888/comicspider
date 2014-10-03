from bs4 import BeautifulSoup
import urllib2
import re

#getting a webpage

hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

req = response = urllib2.Request('http://www.ishuhui.com/archives/3452', headers=hdr)

try: 
	page = urllib2.urlopen(req)
except urllib2.HTTPError, e:
	print e.fp.read()
#grabbing the content
html = page.read()

soup = BeautifulSoup(html)

soup.prettify()

divs = soup.findAll('h1')

title = divs[0].string.strip()

print title
episode = re.search(r'\d+', title).group()


