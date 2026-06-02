import socket
import threading

def is_port_open(host: str, port: int):
    """Check if the 'host' has any 'port' open """

    # socket creation
    my_socket = socket.socket()

    try:
        # attempts to connect to host using that port aka an address(a machine(host) and a specific door into that machine(port)
        my_socket.connect((host, port)) 
    except (ConnectionRefusedError, TimeoutError, OSError):
        # cannot connect, port is closed
        return False
    else:
        # attempt successful, port is open.
        return True


def main():
    host: str = input("Enter the host: ")

    for port in range(1,65536):
        if is_port_open(host, port):
            print(f"{host}:{port} is open")

if __name__ == "__main__":
    main()
