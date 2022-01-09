from easysockets import ClientSocket


# Create a client socket object
client = ClientSocket()

# Connect to localhost:8080
connection = client.connect(host="localhost", port=8080)

# Send "Hey there!"
connection.send(b"Hey there!")

# Print the message we get back
print(connection.receive().decode())

# Send "Bye!"
connection.send(b"Bye!")

# Print the message we get back
print(connection.receive().decode())

# Close the connection (NOTE: This isn't necessary if you end the program but it's good practice to do it anyway)
connection.close()
