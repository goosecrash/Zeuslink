import websocket_server

# Define a function to handle incoming messages
def on_message(client, server, message):
    print(f"received message from {client['address']}: {message}")

# Create a websocket server
server = websocket_server.WebSocketServer("0.0.0.0", 8000, on_message=on_message)

# Start the server
server.run_forever()
