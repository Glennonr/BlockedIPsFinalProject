import requests
from ip2geotools.databases.noncommercial import DbIpCity
import matplotlib.pyplot as plt

longitudes = []
latitudes = []
iplist = []
old_list = []


def get_from_flask():
    response = requests.get("http://127.0.0.1:5000/get")
    response.raise_for_status()
    data = response.json()
    return data['ips']


def pop_ips_to_long_lat():
    ip = iplist.pop()
    try:
        response = DbIpCity.get(ip, api_key='free')
        return response.latitude, response.longitude
    except KeyError:
        return None, None


def plot_point(longitude, latitude):
    if longitude is not None or latitude is not None:
        plt.scatter(float(longitude), float(latitude), c='red', alpha=.75, s=10)


if __name__ == '__main__':
    while True:
        iplist = get_from_flask()
        plt.ion()
        img = plt.imread("RealisticMap.jpg")
        plt.imshow(img, extent=[-180, 180, -90, 90])
        plt.show()
        if len(longitudes) != 0 and len(latitudes) != 0:
            plt.scatter(latitudes, longitudes, c='black', alpha=.75, s=10)
            longitudes.clear()
            latitudes.clear()
        while len(iplist) != 0:
            longitude, latitude = pop_ips_to_long_lat()
            if latitude is not None and latitude is not None:
                print(latitude)
                print(longitude)
                longitudes.append(longitude)
                latitudes.append(latitude)
                plot_point(latitude, longitude)
                plt.show()
                plt.pause(0.001)
                print('plotted')
        plt.clf()
