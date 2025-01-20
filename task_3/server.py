from socket import socket, AF_INET, SOCK_STREAM
from select import select
from struct import Struct

server_addr = ('localhost', 12000)

packer = Struct("20s i ?")
packer2 = Struct("10s")

with socket(AF_INET, SOCK_STREAM) as server:
    inputs = [server]
    server.bind(server_addr)
    server.listen(5)

    while True:
        timeout = 1
        r, w, e = select(inputs, inputs,inputs,timeout)
        
        if not (r or w or e):
            continue
        
        for s in r:
            if s is server:
                client, client_addr = s.accept()
                inputs.append(client)
                print("Csatlakozott:",client_addr)
            else:
                data = s.recv(packer.size)
                if not data:
                    inputs.remove(s)
                    s.close()
                    print("kliens kilepett")
                else:    
                    string, num, bool = packer.unpack(data)
                    string = string.decode()
                    print("Kaptam:", string, str(num), str(bool))
                    result = ""
                    if bool:
                        result = string[0:num]
                    else:
                        result = string[-num:]
                    print(result)
                    data = packer2.pack(result.encode())
                    s.sendall(data)
                    
                    

