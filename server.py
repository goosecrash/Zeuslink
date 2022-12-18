import asyncio
import websockets

async def main():
    # Connect to the websocket server
    uri = "[Zeuslink].[goosecrash].[repl].[co]"
    async with websockets.connect(uri) as websocket:
        # Send a message to the server
        message = "Hello from the client!"
        await websocket.send(message)
        print(f'Sent message: {message}')

        # Receive the response from the server
        response = await websocket.recv()
        print(f'Received response: {response}')

# Run the main function
asyncio.run(main())

async def handle_connection(websocket, path):
    print("Client connected")  # Print a confirmation message

    # Send the server confirmation message to the client
    confirmation_message = "Welcome to zeuslink\nNumber of CPUs: {}\nThe current time is: {}".format(num_cpus, time_str)
    await websocket.send(confirmation_message)

    # Process incoming message
    message = await websocket.recv()
    print(f'Received message: {message}')

    # Run the main function and get the result
    result = main()

    # Send the result back to the client
    await websocket.send(result)
