
    
import socket
    
    
TCP_IP = '127.0.0.1'
TCP_PORT = 18
BUFFER_SIZE = 20  
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
   
conn, addr = s.accept()
print('Connection address:', addr)
while 1:
       data = conn.recv(BUFFER_SIZE)
       if not data: break
       print("received data:", data)
       conn.send(data)  
conn.close()

import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 18
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
   
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()
   
print("received data:", data);

