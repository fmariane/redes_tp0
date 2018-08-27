# USED AS REFERENCE https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
# README deste programa esta no repositorio do github https://github.com/fmariane/redes_tp0/blob/wip/README.md

import socket
import struct
import sys
import threading

#====== Redes de computadores
#====== TP0 - introducao a programacao com sockets
#====== MARIANE FERNANDES DE OLIVEIRA


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
HOST = ''                 # Não precisa indicar o endereço (é o da máquina local)
PORT = int( sys.argv[1] ) # Porta que o servidor deve ficar
orig = (HOST, PORT)

# Deve primeiro iniciar a abertura passiva com bind e listen
tcp.bind(orig)
tcp.listen(10) #mantem no maximo 10 conexoes em espera

#client_connection defined in while True statement
#this is a worker function
def clientThread(client_connection):
    ack_byte = "ACK".encode('ascii')
    server_output = client_connection.recv(1024).decode('ascii')
    
    #receive from client 
    msg_size = client_connection.recv(32).decode('ascii') #4 byte integer
    client_connection.send(ack_byte)
    
    received = client_connection.recv(int(msg_size))
    client_connection.send(ack_byte)
    
    cypher_key = client_connection.recv(32).decode('ascii')
    client_connection.send(ack_byte)
    
    #decode msg according to caesar_cypher algo and send it back to client
    decoded = caesar_cypher_dec(received, int(cypher_key))
    client_connection.send(decoded.encode('ascii'))
    
    print(server_output)
    
    client_connection.close()

while True:
    client_connection, address = tcp.accept()
    #print('Conectado por', address)
    
    client_worker_thread = threading.Thread(
        target=clientThread,
        args=(client_connection,)
    )
    client_worker_thread.start()