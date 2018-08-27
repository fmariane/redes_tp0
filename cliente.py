# USED AS REFERENCE https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae
# README deste programa esta no repositorio do github https://github.com/fmariane/redes_tp0/blob/wip/README.md

import socket
import struct
import sys

#====== Redes de computadores
#====== TP0 - introducao a programacao com sockets
#====== MARIANE FERNANDES DE OLIVEIRA

def parameterHandler():
    parameter = {
        "server_IP": sys.argv[1],
        "server_PORT": sys.argv[2],
        "msg": sys.argv[3],
        "cypher_key": sys.argv[4],
        "line": sys.argv
    }
    
    return parameter

def ackReceipt(ack):
    if not ack:
        return False
    return True

#======== Encription function ============
def caesar_cypher_enc(str, key):
   #sigma works as a table to shift letters
   sigma = "abcdefghijklmnopqrstuvwxyz"
   aux = []
   for i in range (0, len(str)):
      for j in range(0,26):
         if(str[i] == sigma[j]):
            c = sigma[(j+key)%26]
            aux.append(c)
   #parse list into string
   return ''.join(aux)

#====== Network routines
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# gets parameters passed by command line 
parameter = parameterHandler()

HOST = parameter["server_IP"]          # Endereco IP do servidor
PORT = int(parameter["server_PORT"])   # Porta que o servidor está
dest = (HOST, PORT)
tcp.connect(dest)
print('Conectado! Para sair, use CTRL+X\n')
parameter_list = ' '.join(parameter["line"])
tcp.send(parameter_list.encode('ascii'))

#gets and send string size
str_size = len(parameter["msg"])
tcp.send( str(str_size).encode('ascii') )
ack = tcp.recv(4)
if not ackReceipt(ack):
    print("FAIL TO SEND STRING SIZE!")
   

#if any ack was received, send encoded string
ack = []
int_key = int(parameter["cypher_key"])
str_encoded = caesar_cypher_enc(parameter["msg"], int_key)
tcp.send(str_encoded.encode('ascii'))
ack = tcp.recv(4)
if not ackReceipt(ack):
    print("FAIL TO SEND STRING!")

#send crypt_key and wait for decrypt response
ack = []
tcp.send(parameter["cypher_key"].encode('ascii'))
ack = tcp.recv(4)
response = tcp.recv( int(str_size) )
print("Resposta decifrada pelo servidor: "+response.decode('ascii'))

tcp.close()