import requests
from ip2geotools.databases.noncommercial import DbIpCity
import matplotlib.pyplot as plt

prev_longitudes = []
prev_latitudes = []
ip_list = []


def get_from_flask():
    """
    Using requests, retrieve
    If any status code other than 200, raises an exception
    :return: List of ip addresses
    """
    response = requests.get("http://127.0.0.1:5000/get")
    response.raise_for_status()
    data = response.json()
    return data['ips']


def translate_ip_to_coordinates():
    """
    Pops an IP Address from the global variable ip_list
    and uses DbIpCity to convert it to Longitude and Latitude
    If an error occurs, returns None None
    :return: Latitude, Longitude
    """
    ip = ip_list.pop()
    try:
        response = DbIpCity.get(ip, api_key='free')
        return response.latitude, response.longitude
    except:
        return None, None


def configure_map():
    """
    Create Plot and map background
    """
    plt.ion()
    img = plt.imread("RealisticMap.jpg")
    plt.imshow(img, extent=[-180, 180, -90, 90])
    plt.show()


if __name__ == '__main__':
    while True:
        ip_list = get_from_flask()
        configure_map()
        plt.scatter(prev_latitudes, prev_longitudes, c='red', alpha=.25, s=8)
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
