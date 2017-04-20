import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
	
class Sports_Spider(object):
	
	def generate_sports_pool(self):
		browser = webdriver.PhantomJS()
		browser.get("https://www.premierleague.com/fixtures")
		html = browser.page_source
		soup = BeautifulSoup(p.text,  "html.parser")
		row = soup.find_all("section", class_="fixtures")
		print row
		for one in row[1:]:
			try:
				if one['div']:
					print one
			except:
				continue
					
		return self.ip_pool

if __name__ == '__main__':
	foo = Sports_Spider()
	foo.generate_sports_pool()
