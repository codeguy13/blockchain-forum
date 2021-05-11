import socket, threading, json, sys


class NodeServer:
    def __init__(self):
        self.port = 9736
        self.host = ''
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start_up(self):
        try:
            self.sock.bind((self.host, self.sock))
        except socket.error:
            print("Bind failed")
            sys.exit()

        self.sock.listen(3)
        print("Opened listening socket")

        while True:
            conn, address = self.sock.accept()
            print(f"Connected to {address[0]}")
