from util import timefunc
from port_scanner import Scanner
from grabber import Grabber


@timefunc
def main():
    ip = '13.245.12.219'
    portrange = (20, 25)
    scanner = Scanner(ip)
    scanner.scan(*portrange)
    for port in scanner.open_ports:
        try:
            grabber = Grabber(ip, port)
            print(grabber.read())
            grabber.close()
        except Exception as e:
            print(f"error: {e}")


if __name__ == '__main__':
    main()
