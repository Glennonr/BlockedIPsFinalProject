from redis import Redis

from ip2geotools.databases.noncommercial import DbIpCity

r = Redis()


def file_to_redis(filename):
    with open(filename, 'r') as f:
        if r.llen('iplist') != 0:
            r.delete('iplist')
        for line in f:
            attack_date, attack_time, attack_ip, attack_protocol = line.split()
            print(attack_ip)
            print(type(attack_ip))
            r.lpush("iplist", attack_ip)
        print(r.llen("iplist"))


def pop_ips_to_long_lat():
    ip = r.lpop("iplist")
    response = DbIpCity.get(ip, api_key='free')
    return response.latitude, response.longitude


if __name__ == '__main__':
    file_to_redis("BlockedIPs.txt")
    while r.llen("iplist") != 0:
        print(pop_ips_to_long_lat())

# import socket
# import sys

# # 10.230.1.59
# # Create a TCP/IP socket for receiving data
# RCV_UDP_IP = "10.230.1.59"
# RCV_UDP_PORT = 5140
#
# # Bind the socket to the port
# rcv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
# rcv_sock.bind((RCV_UDP_IP, RCV_UDP_PORT))
#
# while True:
#     # Receive message
#     data, address = rcv_sock.recvfrom(1024)
#
#     # Parse original message and create a new one
#     # syslogmsg = data.split(",")
#     # print >> sys.stderr, syslogmsg
#     print(data, address)
#
#     # Instead of print, push into list on Redis
