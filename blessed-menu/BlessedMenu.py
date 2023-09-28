from blessed import Terminal

class BlessedMenu:
    MenuItems = []
    SelectedItemIndex = 0

    def __init__(self, terminal):
        self.Terminal = terminal

    def AddItem(self, MenuItem):
        self.MenuItems.append(MenuItem)

    def MoveUp(self):
        if len(self.MenuItems) < 1:
            return

        if self.SelectedItem > 1:
            self.SelectedItemIndex = self.SelectedItem - 1

        self.SelectedItem.UnsetSelected()
        self.SelectedItem = self.MenuItems[self.SelectedItem]
        self.SelectedItem.SetSelected()
    
    def MoveDown(self):
        if len(self.MenuItems) < 1:
            return

        if self.SelectedItem < len(self.MenuItems - 1):
            self.SelectedItemIndex = self.SelectedItem + 1

        self.SelectedItem.UnsetSelected()
        self.SelectedItem = self.MenuItems[self.SelectedItem]
        self.SelectedItem.SetSelected()

    def Display(self):
        self.SelectedItemIndex = 0
        self.SelectedItem = self.MenuItems[0]
        self.SelectedItem.SetSelected()

        for item in self.MenuItems:
            item.Display(self.Terminal)
