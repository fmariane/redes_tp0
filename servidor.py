# USED AS REFERENCE https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae

import socket
import struct
import sys
import threading

#======== Decription function
def caesar_cypher_dec(str, key):
    #sigma works as a table to shift letters
    sigma = "abcdefghijklmnopqrstuvwxyz"
    aux = []
    for i in range (0, len(str)):
        for j in range(0,26):
            if(str[i] == sigma[j]):
                c = sigma[(j-key)%26]
                aux.append(c)
    #join method parse list into string
    return ''.join(aux)

#====== Network routines ==============
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ''              # Não precisa indicar o endereço (é o da máquina local)
PORT = 5000            # Porta que o servidor deve ficar
orig = (HOST, PORT)

# Deve primeiro iniciar a abertura passiva com bind e listen
tcp.bind(orig)
tcp.listen(10) #mantem no maximo 10 conexoes em espera

# Agora está pronto para receber uma conexão vinda de um cliente
#con, cliente = tcp.accept()


#client_connection defined in while True statement
def clientThread(client_connection):
    ack_byte = "ACK".encode('ascii')
    
    #receive from client 
    msg_size = client_connection.recv(32) #4 byte integer
    client_connection.send(ack_byte)
    
    received = client_connection.recv(int(msg_size))
    client_connection.send(ack_byte)
    
    cypher_key = client_connection.recv(32)
    client_connection.send(ack_byte)
    
    #decode msg according to caesar_cypher algo and send it back to client
    decoded = caesar_cypher_dec(received, cypher_key)
    client_connection.send(decoded.encode('ascii'))
    client_connection.close()

while True:
    client_connection, address = tcp.accept()
    print('Conectado por', address)
    
    client_worker_thread = threading.Thread(
        target=clientThread,
        args=(client_connection,)
    )
    client_worker_thread.start()