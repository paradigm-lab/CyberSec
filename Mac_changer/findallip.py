import nmap


class Network(object):
    def __init__(self):
        ip = input("Please Enter IP Default is 192.168.1.1/192.168.0.1: ")
        self.ip = ip

    def networkScanner(self):
        if len(self.ip) == 0:
            network = '192.168.1.1/24'
        else:
            network = self.ip + '/24'

        print("Scanning Please wait......")
