# DCC023 Redes de Computadores TP0
## Conceitos básicos de sockets
### Comunicação cliente-servidor usando TCP 

Pontos relevantes:
```python
tcp.listen(10)
```
A linha acima na verdade não tem muito efeito. Poderia ser listen(1), porque como não há limite de threads, sempre que um cliente chegar ele será atendido  

```python
client_worker_thread = threading.Thread(target=clientThread, args=(client_connection,) )
```
Esta linha atribui a conexão do cliente a uma thread que fará o trabalho de atendê-lo. Todas as threads são processadas pela mesma função `clientThread`. 
O requisito do trabalho é atendido em 
```python
received = client_connection.recv(int(msg_size))  #recebe a mensagem codificada de tamanho mg_size
decoded = caesar_cypher_dec(received, cypher_key) #decifra a tring recebida de acordo com a Cifra de Caesar
client_connection.send(decoded.encode('ascii'))   #envia a mensagem decodificada para o cliente
```



Utilizei um **_dummy ack_**, quero dizer, não utilizei o sinal de AK do próprio protocolo, só escrevi uma mensagem qualquer e enviei, o que pode ser um grande problema numa aplicação real porque este tipo de confimação está tão sujeita a falha quando o envio do dado.

```python
def ackReceipt(ack): #ack é uma string
    if not ack:
        return False
    return True
```


Código usado como referência: https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae

