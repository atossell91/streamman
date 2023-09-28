import socket

from NetworkModule import NetworkModule

class Client(NetworkModule):
    def __init__(self):
        self.socket = None

    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((self.host, self.port))

c = Client()
c.load_configs()
c.start()
c.cleanup()
