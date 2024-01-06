#server 
import socket
import random
import threading

#function to handle client
def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Recived message from client : {data}")
    random_values = random.randint(1,100)
    client_socket.send(str(random_values).encode('utf-8'))
    client_socket.close()

#start server file

def start_server():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('0.0.0.0',5000))
    server.listen(5)
    print("Seerver Listening on the port 5000")
    while True:
        client, addr = server.accept()
        print(f"Accpted Connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client,args=(client,))
        client_handler.start()

if __name__ == "__main__":
    start_server()


