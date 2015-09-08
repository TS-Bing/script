#/usr/bin/env python
#coding:utf-8

import requests,sys,re
from BeautifulSoup import BeautifulSoup
from tld import get_tld

result_urls = []
def get_url(page):
	urls = []
	#http://www.wooyun.org/corps/page/1
	headers = {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)'}
	r = requests.get('http://www.wooyun.org/corps/page/%s' % page,headers=headers)
	htmlpage = r.text

	soup = BeautifulSoup(htmlpage)
	for result_table in soup.findAll('a'):
		url = result_table.get("href")
		try:
			if re.findall(r'wooyun.org',url) or re.findall(r'miibeian.gov.cn',url):
				pass
			else:
				urls.append(get_tld(url))
		except:
			pass
	return urls


if __name__ == '__main__':
	list = raw_input("请输入获取乌云厂商的页数：")
	result_urls1 = []
	list = int(list)+1
	if int(list) == 0:
		sys.exit(0)
	f = open('wooyun.txt','a')
	for i in range(0,int(list)):
		result_urls = get_url(i)
		for j in result_urls:
			f.writelines(j)
			f.writelines('\n')
	#print result_urls1