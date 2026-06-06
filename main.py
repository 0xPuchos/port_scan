import threading
import socket
import threading

print_lock = threading.Lock()

def is_port_open(host: str, port: int):
    """Check if the 'host' has any 'port' open """

    # socket creation
    my_socket = socket.socket()

    try:
        # attempts to connect to host using that port aka an address(a machine(host) and a specific door into that machine(port)
        my_socket.connect((host, port)) 
    except (ConnectionRefusedError, TimeoutError, OSError):
        # cannot connect, port is closed
        return 
    else:
        # attempt successful, port is open.
        with print_lock:
            print(f"{host}:{port} is open")


def main():
    host: str = input("Enter the host: ")
    threads: list = []

    for port in range(1,65536):
       t = threading.Thread(target=is_port_open,args=(host,port))
       threads.append(t)
       t.start()

    # wait for all threads to finish
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
