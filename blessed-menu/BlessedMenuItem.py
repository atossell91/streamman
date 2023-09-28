from blessed import Terminal

class BlessedMenuItem:

    IsSelected = False

    def __init__(self, text):
        self.text = text
    
    def SetSelected(self):
        self.IsSelected = True
    
    def SetUnselected(self):
        self.IsSelected = False

    def Display(self, terminal):
        if self.IsSelected:
            print(terminal.orange_on_black + self.text)
        else:
            print(terminal.white_on_black + self.text)
