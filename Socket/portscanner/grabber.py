from util import timefunc

import socket


class Grabber:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(0.3)
        self.socket.connect((self.ip, self.port))

    def read(self, length=1024):
        return self.socket.recv(length)

    def close(self):
        self.socket.close()


@timefunc
def main():
    grabber = Grabber('13.245.12.219', 22)
    print('checking ...')

    try:
        print(grabber.read())
    except Exception as e:
        print(e)

    print('done ...')
    grabber.close()


if __name__ == '__main__':
    main()
