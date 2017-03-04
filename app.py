from IP_Spider import IP_Spider
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def getIpPair():
	spider = IP_Spider()
	ip = spider.generate_ip_pool()
	return jsonify(result=[e.serialize() for e in ip])
	
if __name__ == '__main__':
    app.run()
	