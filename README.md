# DCC023 Redes de Computadores TP0
## Conceitos básicos de sockets
### Comunicação cliente-servidor usando TCP 

Pontos relevantes:
```python
tcp.listen(10)
```
A chamada do `listen` indica que o servidor está pronto para aceitar conexões. O parâmetro 10 indica que até 10 conexões podem permanecer aguardando para passar pelo `bind`. No caso desta implementação não haverá clientes esperando, porque sempre que um cliente se apresenta, ele é conectado e uma thread passa a atendê-lo.


```python
client_worker_thread = threading.Thread(target=clientThread, args=(client_connection,) )
```
Esta linha atribui a conexão do cliente a uma thread que fará o trabalho de atendê-lo. Todas as threads são processadas pela mesma função `clientThread`. 
O requisito do trabalho é atendido em 
```python
received = client_connection.recv(int(msg_size))  #recebe a mensagem cifrada de tamanho msg_size
decoded = caesar_cypher_dec(received, cypher_key) #decifra a tring recebida de acordo com a Cifra de Caesar
client_connection.send(decoded.encode('ascii'))   #envia a mensagem decifrada para o cliente
```

Código usado como referência: https://gist.github.com/Integralist/3f004c3594bbf8431c15ed6db15809ae

