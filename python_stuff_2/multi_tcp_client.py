#!/usr/bin/python3

import sys 
from socket import socket, AF_INET, SOCK_STREAM

import sys
from socket import socket, SOCK_STREAM, AF_INET

def main():  
     quit = False
     if len(sys.argv) >= 3:    
         ip = sys.argv[1]    
         port = int(sys.argv[2])    
     data = None  
     while quit == False:    
         data = sys.stdin.readline()    
         print("Will send %s to %s:%d via tcp" % (data, ip, port))   
         tcp_sock = socket(AF_INET, SOCK_STREAM)

         try:    
             tcp_sock.connect((ip, port))    
             print("Connect succeeded.")  
         except ConnectionRefusedError as e:    
             print("Failed to connect!")    
             sys.exit(1)  
         try:    
             tcp_sock.send(bytes(data, 'utf-8'))    
             indata = tcp_sock.recv(1024)    
             print(indata.decode('utf-8'))  
         except KeyboardInterrupt as e:    
             print("Got keyboard kill")
             quit = True   
         finally:    
             tcp_sock.close()


if __name__ == "__main__":  main()
