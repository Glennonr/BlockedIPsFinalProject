from redis import Redis
from flask import Flask, jsonify

r = Redis()

app = Flask(__name__)


@app.route('/get', methods=["GET"])
def get_from_redis():
    out_iplist = r.hkeys("iphash")
    decode_list = [x.decode('utf-8') for x in out_iplist]
    for ip in out_iplist:
        decode_list.append(ip.decode())

    out = {'ips': str(out_iplist)}
    return out, 200


if __name__ == '__main__':
    app.run(port=5000)
