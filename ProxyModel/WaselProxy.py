import requests
from bs4 import BeautifulSoup
from BaseProxy import BaseProxy

class WaselProxy(BaseProxy):
	def get_proxy_ip(self):
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
						country = x[2].find_all("span")[1].text
						if country in self.country_whitelist:
							self.ip_pool.append("{}:{}".format(x[0].text,x[1].text))
				except:
					continue
					
		return self.ip_pool