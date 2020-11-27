import socket
import sys
from redis import Redis

r = Redis()

# 10.230.1.59
# Create a TCP/IP socket for receiving data
RCV_UDP_IP = "10.230.1.59"
RCV_UDP_PORT = 5140

# Bind the socket to the port
rcv_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
rcv_sock.bind((RCV_UDP_IP, RCV_UDP_PORT))

while True:
    # Receive message
    data, address = rcv_sock.recvfrom(1024)

    # Parse original message and create a new one
    # syslogmsg = data.split(",")
    # print >> sys.stderr, syslogmsg
    print(data, address)

    # Instead of print, push into list on Redis
    r.delete('iphash')
    attack_ip = address
    r.hset('iphash', attack_ip, attack_time)
    ip_dict = r.hgetall('iphash')
    for ip in ip_dict:
        iterated_time = int(ip_dict[ip].decode()[6:])
        time_to_add = int(attack_time[6:])
        print(iterated_time, time_to_add)
        if iterated_time - time_to_add < 0:
            r.hdel('iphash', ip)
            print('deleted', ip)