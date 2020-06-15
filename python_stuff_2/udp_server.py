#!/usr/bin/python3

import sys 
from socket import socket, AF_INET, SOCK_DGRAM

ip = sys.argv[1]
port = int(sys.argv[2])
udp_sock = socket(AF_INET, SOCK_DGRAM)
udp_sock.bind((ip, port))
while True:
    data, (client_ip, client_port) = udp_sock.recvfrom(100)
    print("Received %d bytes from %s:%d" % (len(data), client_ip, client_port))
    print(data)
    udp_sock.sendto(data, (client_ip, client_port))
    
