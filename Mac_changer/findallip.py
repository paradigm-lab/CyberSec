import nmap


class Network(object):
    def __init__(self):
        ip = input("Please Enter Default Ip Address of Router: ")
        self.ip = ip
