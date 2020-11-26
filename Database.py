from redis import Redis
from ip2geotools.databases.noncommercial import DbIpCity
import matplotlib.pyplot as plt

r = Redis()


def file_to_redis(filename):
    with open(filename, 'r') as f:
        if r.llen('iplist') != 0:
            r.delete('iplist')
        for line in f:
            attack_date, attack_time, attack_ip, attack_protocol = line.split()
            print(attack_ip)
            r.lpush("iplist", attack_ip)


def pop_ips_to_long_lat():
    ip = r.lpop("iplist")
    response = DbIpCity.get(ip, api_key='free')
    return response.latitude, response.longitude


def plot_point(longitude, latitude):
    if longitude is not None or latitude is not None:
        plt.scatter(float(longitude), float(latitude), c='red', alpha=0.5, s=10)


if __name__ == '__main__':
    file_to_redis("BlockedIPs.txt")
    plt.ion()
    img = plt.imread("RealisticMap.jpg")
    plt.imshow(img, extent=[-180, 180, -90, 90])
    plt.show()
    while r.llen("iplist") != 0:
        longitude, latitude = pop_ips_to_long_lat()
        plot_point(latitude, longitude)
        plt.show()
        plt.pause(0.001)
