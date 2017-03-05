import requests
from bs4 import BeautifulSoup
from BaseProxy import BaseProxy

class ListPlusProxy(BaseProxy):
	def get_proxy_ip(self):
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