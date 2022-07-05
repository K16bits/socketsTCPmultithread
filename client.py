import socket
from environment import SIZE,PORT
import string
import random

def random_generator(size=SIZE, chars=string.ascii_uppercase + string.digits):
 return ''.join(random.choice(chars) for _ in range(size))

HOST = 'localhost'     
tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)
print ('Client iniciado...')

# msgClient = "Hello World!!"
# 1byte, 512bytes, 1kb,
msgClient = random_generator()

tcp.send(bytes(msgClient,"UTF-8"))

# msg = tcp.recv(SIZE)
# print(msg.decode("UTF-8"))

tcp.close()

#for i in $(seq 1000); do python3 programa.py; done