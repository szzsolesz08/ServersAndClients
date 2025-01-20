from socket import socket, AF_INET, SOCK_DGRAM
from struct import Struct

server_addr = ('oktnb147.inf.elte.hu', 11235)

packer = Struct("10s 6s 20s")

data = packer.pack("UDPKliens".encode(), "gaq4is".encode(), "e2w2x33vfc784uu7".encode())

packer2 = Struct('10s 100s')

with socket (AF_INET, SOCK_DGRAM) as client:
    client.sendto(data, server_addr)

    data,_ = client.recvfrom(packer2.size)
    result = packer2.unpack(data)
    
    str = result[1].decode()
    packer3 = Struct("1s 1s 1s")
    data = packer3.pack(str[3].encode(), str[7].encode(), str[7].encode())

    client.sendto(data, server_addr)

    data,_ = client.recvfrom(packer2.size)
    result = packer2.unpack(data)
    print("Kaptam:", result[1].decode())