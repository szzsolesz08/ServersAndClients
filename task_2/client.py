from socket import socket, AF_INET, SOCK_STREAM
from struct import Struct

server_addr = ('oktnb147.inf.elte.hu', 11224)

packer = Struct("10s 6s 20s")

data = packer.pack("TCPKliens".encode(), "gaq4is".encode(), "u5q8s0aeyo2zg394".encode())

packer2 = Struct('10s 100s')

with socket(AF_INET, SOCK_STREAM) as client:
    client.connect(server_addr)
    client.sendall(data)
    result = client.recv(packer2.size)
    unpacked  = packer2.unpack(result)

    str = unpacked[1].decode()
    packer3 = Struct("1s 1s 1s")
    data = packer3.pack(str[0].encode(), str[2].encode(), str[4].encode())

    client.sendall(data)
    result = client.recv(packer2.size)
    unpacked  = packer2.unpack(result)

    print("Kaptam:", unpacked[1].decode())