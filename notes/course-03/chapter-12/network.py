"""Module for demo of Network, sockets and more"""
import socket

addressTuple = ('data.pr4e.org', 80)

pr4e = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pr4e.connect(addressTuple)
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
pr4e.send(cmd)

while True:
    data = pr4e.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
pr4e.close()