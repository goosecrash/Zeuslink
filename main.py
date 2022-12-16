import random
import os
import dotenv
import asyncio
import websockets
from tqdm import tqdm  # import the tqdm library
import sys
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
# Import the Flask Framework
from flask import Flask, request, render_template, redirect, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room

# Import the Flask-SQLAlchemy library
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from progress.bar import Bar


key = Fernet.generate_key()
async def server():
    # Connect to the WebSocket server
    async with websockets.connect('[Zeuslink].[goosecrash].[repl].[co]') as websocket:
        # Send a message to the server
        await websocket.send('hello')











# Declare variables and functions outside of the while loop to avoid
# recreating them every iteration
operations = ['+', '-', '*', '/']  # list of possible operations
numbers1 = [random.randint(1, 100) for _ in range(6)]  # list of 6 random integers from 1 to 1000
numbers2 = [random.randint(1, 100) for _ in range(6)]  # list of 6 random integers from 1 to 1000
balance = 0
bar = Bar('Processing', max=100)



def main():
    # Choose X and Y outside of the if statement to avoid
    # selecting new random numbers unnecessarily
    X = random.choice(numbers1)
    Y = random.choice(numbers2)
    operation = random.choice(operations)  # choose a random operation from the list
    Z = 0
    if operation == '+':
        Z = X + Y
    elif operation == '-':
        Z = X - Y
    elif operation == '*':
        Z = X * Y
    elif operation == '/':
        Z = X / Y
    Quest1 = 'what does'
    Quest2 = 'equal to:'
    Space1 = " "
    mid = f"{X} {operation} {Y}"  # use f-strings to create the equation string
    print("Welcome to zeuslink")
    MainMenu = input('Press 1 to login or 2 to exit Press 3 for balance')
    start_time = time.time()
    if MainMenu == '1':
         # Generate and solve the equation as before
        print(f"{Quest1} {Space1} {mid} {Space1} {Quest2}")
        Answer = int(input())  # convert user input to integer
        if Answer == Z:  # compare Answer to Z directly
            for i in range(100):
               bar.next()
               time.sleep(0)
               elapsed_time = time.time() - start_time
               print(f'Elapsed time: {elapsed_time:.2f} seconds')
            print("Mined a block")
            global balance
            balance += 5
            print(f'Your balance is: ${balance:.0f}')
            
        else:
            print("error,block not rewarded")
    elif MainMenu == '2':
        # Save balance to wallet.bin file on exit
        with open('wallet.bin', 'w') as f:
            f.write(f'BALANCE={balance}')
        print("Balance saved to wallet")
        exit()
    elif MainMenu == '4':
        print("https://github.com/goosecrash/zeuslink2/tree/main/README.md")
    elif MainMenu == '3':  # new menu option to print balance
        print(f'Your balance is: ${balance:.0f}')

# Load .env file with balance if it exists
if os.path.exists('wallet.bin'):
   with open('wallet.bin', 'rb') as f:
        encrypted_balance = f.read()

while True:
  main()
