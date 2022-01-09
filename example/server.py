from easysockets import ServerSocket, Connection


def handle_client(connection: Connection) -> None:
    """
    Simple echo server.
    """

    print("Client connected")

    # While the connection is open
    while True:
        # Receive data
        data = connection.receive()

        # If the connection is closed, break the loop
        if not data:
            break

        # Print the received data
        print("Received:", data.decode())

        # Echo the received data
        connection.send(data)

    print("Client disconnected")

    # NOTE: You won't have to close the connection manually since it's handled by the server socket object


# Create a server socket object and set the client handler to the function we just created
socket = ServerSocket(
    client_handler=handle_client,
)

# Listen on localhost:8080
socket.listen(host="localhost", port=8080)
