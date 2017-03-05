class BaseProxy:
	def __init__(self):
		self.ip_pool = []
		self.country_whitelist = ["Germany","Canada","United States", "United Kingdom", "France", "Italy", "Netherland","Poland", "Switzerland"]
	
	def get_proxy_ip(self):
		raise NotImplementedError("Subclass must implement abstract method")
