import socket
from environment import SIZE

HOST = 'localhost'     
PORT = 3000       
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)
print ('Client iniciado...')

# msgClient = input('mande uma mensagem para o server TCP: ')
msgClient = "Hello World!!"

# tcp.send(bytes(msgClient,"UTF-8"))
tcp.send(bytes(SIZE))
# msg = tcp.recv(1024)
msg = tcp.recv(1)

print(msg.decode("UTF-8"))
tcp.close()

#for i in $(seq 1000000); do python3 programa.py; done