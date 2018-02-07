import pickle
import socket
import sys

HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(data + "\n")

    # Receive data from the server and shut down
    while True:
        received = sock.recv(1024)
        if not received: break
        print pickle.loads(received)
finally:
    sock.close()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
