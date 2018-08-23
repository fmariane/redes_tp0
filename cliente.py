import socket

HOST = 'localhost'
PORT = 5454

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((HOST, PORT))

#data = s.recv(50)

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

#print("recebi do servodor { " + data.decode('ascii')+ " }")
