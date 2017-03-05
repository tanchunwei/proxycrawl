from IP_Spider import IP_Spider
from flask import Flask, jsonify
app = Flask(__name__)
import json

@app.route("/")
def getIpPair():
	spider = IP_Spider()
	ip = spider.generate_ip_pool()
	return jsonify(ip)
	
if __name__ == '__main__':
    app.run()
	