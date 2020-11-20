from redis import Redis
from flask import Flask, jsonify

r = Redis()

app = Flask(__name__)


@app.route('/get', methods=["GET"])
def get_from_redis():
    out_iplist = r.hkeys("iphash")
    frick = []
    for ip in out_iplist:
        frick.append(ip.decode())
    print(frick)
    print(type(frick))
    out = {'ips': frick}
    return out, 200


if __name__ == '__main__':
    app.run(port=5000)
