import socket
import sys

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
