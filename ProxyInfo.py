class ProxyInfo():

	def __init__(self, ip, country):
		self.ip = ip
		self.country = country
	def serialize(self):
		return {
			'ip' : self.ip,
			'country' : self.country
		}