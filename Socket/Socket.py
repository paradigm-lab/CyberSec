import socket
import argparse
from util import timefunc


class Scanner:
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []

    def __repr__(self):
        return f'Scanner: {self.ip}'

    def add_port(self, port):
        self.open_ports.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((self.ip, port))
        s.close()
        return result == 0

    def write(self, filepath):
        open_ports = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(open_ports))


@timefunc
def main():
    # Creating the argparse object
    parser = argparse.ArgumentParser()

    # Adding the argument action
    # Positional Argument
    # By default the positional Argument are required by default
    # - help for the positional Argument to give the description
    parser.add_argument('ip', help='Pass the Internet protocol(IP) to be scanned ')

    # CLI argument parsing method
    args = parser.parse_args()

    # Getting the argument from the command line and pass the argument into my Scanner class
    scan = Scanner(args.ip)

    # Calling the scan method to scan for the port numbers
    scan.scan(1, 65535)

    # writing the available port numbers into a file
    scan.write('./open_ports')

    # Giving the output of the available ports
    print(scan.open_ports)


if __name__ == "__main__":
    main()
