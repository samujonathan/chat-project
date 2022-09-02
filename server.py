import socket
import threading
from commands import client_commands

s = socket.socket()
# default of socket method is TCP and ipv4
print("Socket Created")

s.bind(('localhost', 9999))
#s.bind binds the port and addr to the server

s.listen(2)
# this queues 2 clients
print("Waiting for connections")

while True:
    c, addr = s.accept()
    
    client = threading.Thread(target=client_commands, args=(c,))
    client.start()

    
