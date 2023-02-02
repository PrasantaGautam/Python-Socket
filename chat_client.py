import socket
import os
import threading

s = socket.socket()

server_ip = "127.0.0.1"
port = 5252

print("Connecting.....")
# s.connect((server_ip, port))

while True:
    try:
        s.connect((server_ip, port))
        print("...Connected...")
        break
    except ConnectionRefusedError:
        pass


def sndmsg():
    while True:
        msg = input("Type -> ")
        if msg != "":
            s.send(msg.encode())
            if msg == "@exit":
                print("You Disconnected !!!")
                os._exit(0)
        else:
            print("Empty Input !")


def rcvmsg():
    while True:
        reply = s.recv(1024)
        if reply.decode() == "@exit":
            print("Server Disconnected !!!")
            os._exit(0)
        print("\nServer : ", reply.decode())


thr1 = threading.Thread(target=sndmsg)
thr1.start()
rcvmsg()
