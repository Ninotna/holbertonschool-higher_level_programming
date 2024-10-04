#!/usr/bin/python3
"""
A simple server and client script to send and receive serialized data 
using sockets. The server listens for incoming connections, receives 
serialized data in JSON format, deserializes it, and prints the received 
dictionary. The client sends a serialized dictionary to the server.
"""

import socket
import json


def start_server():
    """
    Sets up a server that listens for incoming connections on localhost:12345.
    The server receives serialized JSON data from the client, deserializes it,
    and prints the received dictionary.

    The server listens for one connection at a time and handles only one 
    transaction per connection. After receiving and processing the data, 
    the connection is closed.
    """
    # Define host and port for the server
    host = 'localhost'
    port = 12345

    # Create a server socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the host and port
        server_socket.bind((host, port))
        # Set the server to listen for incoming connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        # Wait for a connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            # Receive data from the client
            data = conn.recv(1024)
            if data:
                # Deserialize the received data from JSON format
                received_dict = json.loads(data.decode('utf-8'))
                # Print the received dictionary
                print(f"Received dictionary: {received_dict}")
            else:
                print("No data received")


def send_data():
    """
    Connects to the server running on localhost:12345 and sends a 
    serialized Python dictionary in JSON format.

    The client serializes a dictionary, connects to the server, sends the 
    serialized data, and then closes the connection.
    """
    # Define the server address and port
    host = 'localhost'
    port = 12345

    # Example Python dictionary to send
    data_to_send = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the dictionary into JSON format
    serialized_data = json.dumps(data_to_send)

    # Create a client socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            client_socket.connect((host, port))
            print(f"Connected to server at {host}:{port}")

            # Send the serialized data to the server
            client_socket.sendall(serialized_data.encode('utf-8'))
            print("Data sent successfully")
        except socket.error as e:
            print(f"Socket error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    """
    Main script execution. Prompts the user to start either the server or
    the client based on their input ('s' for server, 'c' for client).
    """
    choice = input("Start server or client? (s/c): ").strip().lower()
    if choice == 's':
        start_server()
    elif choice == 'c':
        send_data()
    else:
        print("Invalid choice. Please enter 's' to start the server or 'c' to run the client.")
