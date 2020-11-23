from redis import Redis
from flask import Flask, jsonify

r = Redis()

app = Flask(__name__)


@app.route('/get', methods=["GET"])
def get_from_redis():
    iplist = r.hkeys("iphash")
    decode_list = [x.decode('utf-8') for x in iplist]
    out = {'ips': decode_list}
    return jsonify(out), 200


if __name__ == '__main__':
    app.run(port=5000)
