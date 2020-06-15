#!/usr/bin/python3

import sys 
from socket import socket, AF_INET, SOCK_DGRAM

client_ip = sys.argv[1]
client_port = int(sys.argv[2])

while True:
    client_data = sys.stdin.readline()
    if client_data == "quit\n":
        udp_client_sock = socket(AF_INET, SOCK_DGRAM)
        ret = udp_client_sock.sendto(bytes(client_data, 'utf-8'), (client_ip, client_port))
        print("Sent %d bytes to %s:%d" % (ret, client_ip, client_port))
        break
    udp_client_sock = socket(AF_INET, SOCK_DGRAM)
    ret = udp_client_sock.sendto(bytes(client_data, 'utf-8'), (client_ip, client_port))
    print("Sent %d bytes to %s:%d" % (ret, client_ip, client_port))
