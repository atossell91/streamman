from BlessedMenu import BlessedMenu
from BlessedMenuItem import BlessedMenuItem
from blessed import Terminal

def main():
    term = Terminal()
    m = BlessedMenu(term)

    itm1 = BlessedMenuItem('Proceed')
    itm2 = BlessedMenuItem('Go back')
    itm3 = BlessedMenuItem('Exit')

    with term.cbreak():
        c = term.inkey()
        if c == term.

if __name__ == '__main__':
    main()
