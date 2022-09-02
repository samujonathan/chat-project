import socket
import threading

c = socket.socket()

c.connect(('localhost', 9999))

name = input("Enter your name ")
c.send(bytes(name, 'utf-8'))
join = c.recv(1024).decode()


if join == "error":
    print("User already exists")
    exit()
else:
    print(join)


def receiver(c):
    while True:
        output = c.recv(1024).decode()
        if output == "exit":
            exit()
        print(output)


receive_handler = threading.Thread(target=receiver, args=(c,))
receive_handler.start()

while True:
    command = input()
    if command.startswith("quit"):
        c.send(bytes("quit:" + command, 'utf-8'))
        break
    else:
        c.send(bytes("msg:" + command, 'utf-8'))
