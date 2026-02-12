import socket
import threading
import sys

def handle_client(client_socket):
    try:
        client_socket.send(b"OK\n")
    finally:
        client_socket.close()

def run_server(host='localhost', port=8080):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(5)
    print(f"Server started on {host}:{port}")
    
    try:
        while True:
            client, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
    except KeyboardInterrupt:
        print("\nServer stopped")
    finally:
        server.close()

if __name__ == "__main__":
    run_server()