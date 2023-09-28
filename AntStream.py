class AntStream:
    def __init__(self, url, name):
        self.name = name
        self.url = url
        self.display_stream = False
    
    def start_recording(self):
        print('Hehehe, I\'m not recording')
    
    def should_display(self):
        self.display_stream = True
    
    def shouldnt_display(self):
        self.display_stream = False
