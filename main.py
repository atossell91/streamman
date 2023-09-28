from AntServer import Server

def main():
    s = Server()
    s.load_configs()
    s.start()

if __name__ == '__main__':
    main()
