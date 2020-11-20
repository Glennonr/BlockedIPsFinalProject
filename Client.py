import requests
from ip2geotools.databases.noncommercial import DbIpCity
import matplotlib.pyplot as plt

prev_longitudes = []
prev_latitudes = []
ip_list = []


def get_from_flask():
    response = requests.get("http://127.0.0.1:5000/get")
    response.raise_for_status()
    data = response.json()
    return data['ips']


def translate_ip_to_coordinates():
    ip = ip_list.pop()
    try:
        response = DbIpCity.get(ip, api_key='free')
        return response.latitude, response.longitude

    except KeyError:
        return None, None


def configure_map():
    plt.ion()
    img = plt.imread("RealisticMap.jpg")
    plt.imshow(img, extent=[-180, 180, -90, 90])
    plt.show()


if __name__ == '__main__':
    while True:
        ip_list = get_from_flask()
        configure_map()
        plt.scatter(prev_latitudes, prev_longitudes, c='black', alpha=.75, s=10)
        prev_latitudes.clear()
        prev_longitudes.clear()

        while len(ip_list) != 0:
            longitude, latitude = translate_ip_to_coordinates()
            if longitude is not None or latitude is not None:
                print(latitude)
                print(longitude)
                prev_longitudes.append(longitude)
                prev_latitudes.append(latitude)
                plt.scatter(latitude, longitude, c='red', alpha=.75, s=10)
                plt.show()
                plt.pause(0.001)

        plt.clf()
