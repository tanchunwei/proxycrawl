import requests
from bs4 import BeautifulSoup
from BaseProxy import BaseProxy

class USProxy(BaseProxy):
	def get_proxy_ip(self):
		get_url = "http://us-proxy.org/"
		p = requests.get(get_url)
		soup = BeautifulSoup(p.content,  "html.parser")
		ip_row = soup.find_all("table", id='proxylisttable')
		ip_row = ip_row[0].find_all("tr")
		
		for one in ip_row[1:]:
			try:
				x = one.find_all("td")
				country = x[3].text
				isHttps = x[6].text
				if country in self.country_whitelist and isHttps == 'yes':
					self.ip_pool.append("{}:{}".format(x[0].text,x[1].text))
			except:
				continue
					
		return self.ip_pool