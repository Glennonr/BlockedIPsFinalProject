from redis import Redis
from flask import Flask, jsonify

r = Redis()

app = Flask(__name__)


@app.route('/get', methods=["GET"])
def get_from_redis():
    """
    Retrieves the iphash from redis with IP keys
    :return: Json with key ips and data [decodeList] and status code 200
    """
    iplist = r.hkeys("iphash")
    decode_list = [x.decode('utf-8') for x in iplist]
    return jsonify({'ips': decode_list}), 200


if __name__ == '__main__':
    app.run(port=5000)
