from enum import Enum
from WaselProxy import WaselProxy
from ListPlusProxy import ListPlusProxy
from USProxy import USProxy
from BaseProxy import BaseProxy

class ProxySelector(Enum):
	waselproxy = 1
	listplusproxy = 2
	usproxy = 4
	all = 7
		
class ProxyFactory:
	def create_proxy(self, selector):
		if(selector == ProxySelector.waselproxy.value):
			return WaselProxy()
		if(selector == ProxySelector.listplusproxy.value):
			return ListPlusProxy()
		if(selector == ProxySelector.usproxy.value):
			return USProxy()
		return NoneProxy()
		
class NoneProxy(BaseProxy):
	def get_proxy_ip(self):
		return []
		
			