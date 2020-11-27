import App
from redis import Redis
import Client
r = Redis()

'''
The redis server must be running in the background for the tests to work correctly.

'''


def test_app_returns_empty_list():
    App.app.config['TESTING'] = True
    r.delete('iphash')
    with App.app.test_client() as client:
        response = client.get('/get').get_json()
        expected = {"ips": []}
        assert response == expected


def test_get_from_redis():
    App.app.config['TESTING'] = True
    r.delete('iphash')
    r.hset('iphash', '14.176.55.163', '23:59:02')
    r.hset('iphash', '187.252.232.250', '23:59:02')
    r.hset('iphash', '88.233.110.106', '23:59:02')
    with App.app.test_client() as client:
        response = client.get('/get').get_json()
        expected = {"ips": ["14.176.55.163", "187.252.232.250", "88.233.110.106"]}
        assert response == expected


def test_client_translate_ip_to_coordinates():
    Client.ip_list = ['14.176.55.163']

    expected = 21.0181246, 105.7791585
    assert Client.translate_ip_to_coordinates() == expected


def test_client_with_invalid_ip_to_coordinates():
    Client.ip_list = ['123']

    expected = None, None
    assert Client.translate_ip_to_coordinates() == expected
