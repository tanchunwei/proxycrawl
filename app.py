from IP_Spider import IP_Spider
from IP_Spider import ProxySelector
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/", defaults={'sel': ProxySelector.all.value})
@app.route("/<int:sel>")
def getIpPair(sel):
	spider = IP_Spider()
	ip_pool = spider.generate_ip_pool(sel)
	return jsonify(ip_pool)
	
if __name__ == '__main__':
    app.run()
	