import socket
import sys

def run_client(host='localhost', port=8080):
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        response = client.recv(1024).decode()
        
        if response == "OK\n":
            print(f"Received correct response: {repr(response)}")
            client.close()
            return 0
        else:
            print(f"Error: incorrect response: {repr(response)}")
            client.close()
            return 1
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_client())