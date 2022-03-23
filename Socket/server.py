import socket


# Private ip Address
# It's going to give you the virtual box ip address
# host = socket.gethostbyname(socket.gethostname())


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    HOST = 'localhost'
    PORT = 8080
    result = server.connect_ex((HOST, PORT))
    print("Result is {}".format(result))
    server.close()


if __name__ == "__main__":
    main()
