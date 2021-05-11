import socket
import sys
from . import node_server


class NodeClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.host = socket.gethostname()
        self.port = 9737

    def find_node(self):
        server = node_server.NodeServer()
        with self.sock as sock:
            for i in server.peer_dict['peer_ip']:
                try:
                    sock.connect((i, self.port))
                    self.send_request()
                    print("Successful connection")
                    data = sock.recv(4096)
                    break
                except socket.error:
                    print(f"Connection to {i} failed, Trying next node")
        print("Data received", repr(data))

    def send_request(self):
        try:
            self.sock.send(str("request").encode('utf-8'))
        except KeyboardInterrupt:
            self.send_disconnect()

    def send_disconnect(self):
        print("Sending disconnect signal")
        self.sock.send(str('q').encode('utf-8'))
        sys.exit()
