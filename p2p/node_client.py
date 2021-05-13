import socket
import sys
from .node_server import NodeServer


class NodeClient(NodeServer):
    """!
    A subclass of node server, Client will have 2 sockets
    'c_sock' is the clients socket
    'sock' is the server socket
    This will be the recipient of the blockchain
    """

    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = socket.gethostname()
    port = 9737

    def find_node(self):
        """!
        Parses the peer list and attempts to connect
        """
        with self.c_sock as sock:
            for i in self.peer_dict['peer_ip']:
                try:
                    sock.connect((i, self.port))
                    self.send_request()
                    print("Successful connection")
                    data = sock.recv(4096)
                    break
                except socket.error:
                    print(f"Connection to {i} failed, Trying next node")
        print("Data received from node", repr(data))

    def send_request(self):
        try:
            self.sock.send(str("request").encode('utf-8'))
        except KeyboardInterrupt:
            self.send_disconnect()

    def send_disconnect(self):
        """!
        Send a disconnect signal to peer
        """
        print("Sending disconnect signal")
        self.sock.send(str('q').encode('utf-8'))
        sys.exit()

    def receive_blockchain(self):
        """!
        Get an up to date copy of the blockchain form one or many nodes
        """
        self.find_node()
        pass
