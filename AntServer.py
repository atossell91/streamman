import socket

from NetworkModule import NetworkModule

class Server(NetworkModule):
    def __init__(self):
        self.simultaneous_cxns = 1
    
    def start(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.bind((self.host, self.port))

        print('Waiting for a connection...')
        sock.listen(self.simultaneous_cxns)

        self.socket, _ = sock.accept()
        print('Connection accepted!')

        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

        print('Socket initialization was successful.')

s = Server()
s.load_configs()
s.start()
s.cleanup()
