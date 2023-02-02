import socket
import os
import threading

s = socket.socket()
server_ip = "127.0.0.1"
port = 5252

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((server_ip, port))
# client_Count = []
s.listen()
print("Listening.....")
conn, addr = s.accept()
print("Connection from: " + str(addr))


def sndmsg():

    while True:
        msg = input("Type -> ")
        if msg != "":
            conn.send(msg.encode())
            if msg == "@exit":
                print("You Disconnected !!!")
                os._exit(0)

        else:
            print("Empty Input !")


def rcvmsg():
    while True:
        reply = conn.recv(1024)
        if reply.decode() == "@exit":
            print("Client Disconnected !!!")
            os._exit(0)
        print("\nClient : ", reply.decode())


thr1 = threading.Thread(target=sndmsg)
thr1.start()
rcvmsg()
thr1.join()




# import socket
# import os
# import threading

# s = socket.socket()

# server_ip = "0.tcp.in.ngrok.io"
# port = 10512
# # print("Connecting.....")

# while True:
#     try:
#         s.connect((server_ip, port))
#         break
#     except ConnectionRefusedError:
#         pass


# def sndmsg():
#     while True:
#         msg = input("Type -> ")
#         if msg != "":
#             s.send(msg.encode())
#             if msg == "@exit":
#                 print("You Disconnected !!!")
#                 os._exit(0)
#         else:
#             print("Empty Input !")


# def rcvmsg():
#     while True:
#         reply = s.recv(1024)
#         if reply.decode() == "@exit":
#             print("Server Disconnected !!!")
#             os._exit(0)
#         print("\nServer : ", reply.decode())


# thr1 = threading.Thread(target=sndmsg)
# thr1.start()
# rcvmsg()
