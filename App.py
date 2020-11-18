from redis import Redis
from flask import Flask, jsonify

r = Redis()

app = Flask(__name__)

out_ipList = []


@app.route('/get', methods=["GET"])
def get_from_redis():
    out = {'ips': out_ipList}
    while r.llen("iplist") != 0:
        ip = (r.lpop("iplist")).decode()
        out_ipList.append(ip)
    return jsonify(out), 200


if __name__ == '__main__':
    app.run(port=5000)
