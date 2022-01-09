# EasySockets
A Python module that allows you to create and use simple sockets.

# Installation
The easysockets module can be installed using pip.
```
pip install easysockets
```
or
```
pip install git+https://github.com/Matthias1590/EasySockets.git
```

You can also install it by cloning this repo and running the following commands
```
python3 setup.py build
python3 setup.py install
```

# Examples
The easysockets module contains 3 main classes: ServerSocket, ClientSocket and Connection. Below are examples on how to use each of them.
```py
# The ServerSocket class is used to create a server socket, to create an instance of the ServerSocket class you need a client handler, a client handler is a function that will be passed a connection, the client handler function can then, as the name suggests, handle the client/connection
server_socket = ServerSocket(client_handler=lambda connection: connection.send(b"Hello, world!"))  # This handler just sends "Hello, world!" and then closes the connection

# To make the server socket listen, use the "listen" method. You'll have to specify a host and port
server_socket.listen(host="localhost", port=8080)

# Now whenever a client connects, the lambda we made earlier will be called and will send "Hello, world!" to the client after which it'll close the connection
```
```py
# The ClientSocket class is used to connect to server sockets
client_socket = ClientSocket()

# To connect to a server, use the "connect" method. You'll have to specify the host and port the server is hosted on. This will return a connection that you can then use to communicate with the server
connection = client.connect(host="localhost", port=8080)

# Sending "Hey!" to the server
connection.send(b"Hey!")

# Receiving a message and printing it (NOTE: The message will be received as bytes, to turn it into a string you can use the decode method)
print(connection.receive().decode())

# Closing the connection (NOTE: This isn't necessary if you end the program but it's good practice to do it anyway)
connection.close()
```
```py
# Assume that we just connected to a server
...

# The Connection class is used to communicate to a server/client, whenever you connect to a server or have a client connect to you, you will be given a Connection instance, you cannot create Connections using the constructor

# Send a message (you can only send bytes, if you want to send a string, just encode it)
connection.send("Hello".encode())
# is the same as
connection.send(b"Hello")

# Receive a message
message = connection.receive()
print(message.decode())

# Closing the connection
connection.close()
```

For more examples, check out `example/client.py` and `example/server.py`

# Downloads
[![Downloads](https://pepy.tech/badge/easysockets)](https://pepy.tech/project/easysockets) [![Downloads](https://pepy.tech/badge/easysockets/month)](https://pepy.tech/project/easysockets) [![Downloads](https://pepy.tech/badge/easysockets/week)](https://pepy.tech/project/easysockets)

# Supported Operating Systems
The easysockets module is supported on every operating system as it only uses the built-in `socket` module.