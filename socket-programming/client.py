#CLIENT
import socket

#start client function
def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 5000))
    message = "hello from the client"
    client.send(message.encode('utf-8'))
    random_values = client.recv(1024).decode('utf-8')
    print(f"Recived the Random Values from the server: {random_values}")
    client.close()

if __name__ == "__main__":
    start_client()

