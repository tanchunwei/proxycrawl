# Author: Hao in UT Austin
# Crawle free proxy IPs from http://www2.waselproxy.com/, https://nordvpn.com/free-proxy-list/, https://www.hide-my-ip.com/proxylist.shtml
# Output: list oject, ip_pool
import requests
from bs4 import BeautifulSoup
import json

class IP_Spider(object):
	def __init__(self):
		self.ip_pool = []
		self.country_whitelist = ["Germany","Canada","United States", "United Kingdom", "France", "Italy", "Netherland","Poland", "Switzerland"]

	def get_proxy_from_waselproxy(self):
		# Crawl from http://www2.waselproxy.com/
		for page in range(1,3):
			get_url = "http://www2.waselproxy.com/page/" + str(page)
			p = requests.get(get_url)					
			soup = BeautifulSoup(p.content,  "html.parser")
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

	def get_proxy_from_proxylistplus(self):

		# Crawl from https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-1
		for page in range(1, 11):
			get_url = "https://list.proxylistplus.com/Fresh-HTTP-Proxy-List-" + str(page)
			p = requests.get(get_url)
			soup = BeautifulSoup(p.content, "html.parser")
			ip_row = soup.find_all("tr", {"onmouseout":"this.className='cells'"})

			for one in ip_row:
				try:
					x = one.find_all("td")
					https = x[6].text
					if https == "no":
						continue

					country = x[4].text
					if country in self.country_whitelist:
						self.ip_pool.append("{}:{}".format(x[1].text,x[2].text))
				except:
					continue
		return self.ip_pool
	
	def generate_ip_pool(self):	

		#return self.get_proxy_from_waselproxy()
		return self.get_proxy_from_proxylistplus()

if __name__ == '__main__':
	foo = IP_Spider()
	x = foo.generate_ip_pool()
	print(len(x))
	print(x)
