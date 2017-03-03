# Author: Hao in UT Austin
# Crawle free proxy IPs from http://www2.waselproxy.com/, https://nordvpn.com/free-proxy-list/, https://www.hide-my-ip.com/proxylist.shtml
# Output: list oject, ip_pool
import requests
from bs4 import BeautifulSoup
import json

class IP_Spider(object):
	def __init__(self):
		self.ip_pool = []
		pass
	def generate_ip_pool(self):	
		# Crawl from http://www2.waselproxy.com/
		for page in range(1,3):
			get_url = "http://www2.waselproxy.com/page/" + str(page)
			p = requests.get(get_url)					
			soup = BeautifulSoup(p.content,  "lxml")
			ip_row = soup.find_all("tr")

			for one in ip_row[1:]:
				try:
					x = one.find("progress")
					value = int(x.get('value'))
					if value >= 50:
						x = one.find_all("td")
						ip = "http://" + x[0].text + ":" + x[1].text
						country = x[2].find_all("span")[1].text
						self.ip_pool.append((ip,country))
				except:
					continue
					
		return self.ip_pool

if __name__ == '__main__':
	foo = IP_Spider()
	x = foo.generate_ip_pool()
	print len(x)
	print x
