import socket
import threading
from environment import SIZE

def thread_function(conn):
    with conn:
        # msg = conn.recv(1024)
        msg = conn.recv(SIZE)
        if not msg:
            return conn.close()

        print("Client{} Message:{}".format(client,msg.decode("UTF-8")))
        print("Finalizando a conexão com o cliente")
        # stringReverse = msg[::-1]
        # conn.sendall(stringReverse)
        conn.close()

HOST = 'localhost'
PORT = 3000

tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
orig = (HOST,PORT)
tcp.bind(orig)
tcp.listen(1)

print("Server TCP está rodando...")
while True:
    conn,client = tcp.accept()
    print("Cliente conectado: ",client)
    threadProcess = threading.Thread(target=thread_function,args=(conn,))
    threadProcess.start()
