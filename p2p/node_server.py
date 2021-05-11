import socket
import sys


class NodeServer:
    def __init__(self):
        self.peer_dict = {"peer_ip": []}
        self.port = 9736
        self.host = socket.gethostname()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start_up(self):
        try:
            self.sock.bind(('', self.port))
        except socket.error:
            print("Bind failed")
            sys.exit()

        self.sock.listen(3)
        print("Opened listening socket")

        conn, address = self.sock.accept()
        with conn:
            while True:
                print(f"Connected to {address[0]}")
                self.peer_dict['peer_ip'].append(address[0])
