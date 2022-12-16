import asyncio
import websockets

async def main(websocket, path):
    # This function will be called for each websocket connection that is established
    message = await websocket.recv()  # receive a message from the client
    print(f"Received message: {message}")
    response = "Hello, client!"  # create a response to send back to the client
    await websocket.send(response)  # send the response back to the client

# Set up the websocket server
async def start_server():
    server = await websockets.serve(main, '[Zeuslink].[goosecrash].[repl].[co]', 8000)
    await server.wait_closed()

# Run the websocket server in the event loop
asyncio.get_event_loop().run_until_complete(start_server())
asyncio.get_event_loop().run_forever()
