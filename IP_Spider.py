import json
from ProxyModel.Proxy import ProxySelector, ProxyFactory
	
class IP_Spider(object):
	
	def generate_ip_pool(self, sel):
		proxyList = []
		
		for ps in ProxySelector:
			if ps !=  ProxySelector.all:
				proxy = ProxyFactory().create_proxy(sel & ps.value)
				proxyList.append(proxy)
		
		proxyIp = []
		for proxy in proxyList:
			proxyIp += proxy.get_proxy_ip()
		return proxyIp

if __name__ == '__main__':
	foo = IP_Spider()
	x = foo.generate_ip_pool(ProxySelector.all.value)
	print(len(x))
	print(x)
