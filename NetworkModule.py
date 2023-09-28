import json
import socket

cxn_config_file = 'cxn-info.json'

class NetworkModule:
    def __init__(self):
        self.host = None
        self.port = None

        self.socket = None

    def load_configs(self):
        
        with open(cxn_config_file) as cxn_file:
            cxn_config = json.load(cxn_file)
        
        self.host = cxn_config['host']
        self.port = cxn_config['port']

    def cleanup(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print('Socket was shut down')
