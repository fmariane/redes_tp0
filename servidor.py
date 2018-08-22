import socket
import time

HOST = 'localhost'
PORT = 5454

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

data = input()

#encode function
def enc(str, key):
    #works as a table to shift letters
    sigma = "abcdefghijklmnopqrstuvwxyz"
    aux = []
    for i in range (0, len(str)):
        for j in range(0,25):
            if(str[i] == sigma[j]):
               c = sigma[(j+key)%25]
               aux.append(c)
    #parse list into string
    return ''.join(aux)


encoded_data: str = enc(data, 1)
s.sendto(encoded_data.encode('ascii'), (HOST, PORT) )
