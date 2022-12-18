import random
import os
import dotenv
from cryptography.fernet import Fernet
import psutil
from tqdm import tqdm
import os
from multiprocessing import cpu_count
from multiprocessing import Pool
import time
import ecdsa
import datetime
import json







num_cpus = os.cpu_count()
now = datetime.datetime.now()
time_str = now.strftime("%I:%M %p")
# Declare variables and functions outside of the while loop to avoid
# recreating them every iteration
operations = ['+', '-', '*', '/']  # list of possible operations
numbers1 = [random.randint(1, 100) for _ in range(6)]  # list of 6 random integers from 1 to 1000
numbers2 = [random.randint(1, 100) for _ in range(6)]  # list of 6 random integers from 1 to 1000
balance = 0

# Check if key.bin and wallet.bin exist
if not os.path.exists('key.bin') or not os.path.exists('wallet.bin'):
    # Generate a new key for the Fernet algorithm
    key = Fernet.generate_key()
    fernet = Fernet(key)
    sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
    vk = sk.get_verifying_key()
    public_key = vk.to_string()
    # Write the key to key.bin
    with open('public_key.bin', 'wb') as f:
        f.write(public_key)

  

    # Write the key to key.bin
    with open('key.bin', 'wb') as f:
        f.write(key)
    
    # Encrypt and write some sample data to encrypted.bin
    encrypted_data = fernet.encrypt(b'Some sensitive data')
    with open('encrypted.bin', 'wb') as f:
        f.write(encrypted_data)

# Loads the wallet.bin if it exists
if os.path.exists('wallet.bin'):
    # Read the key from key.bin
    with open('key.bin', 'rb') as f:
        key = f.read()
    
    # Initialize the Fernet object with the key
    fernet = Fernet(key)
    
    # Read the encrypted balance from wallet.bin and decrypt it
    with open('wallet.bin', 'rb') as f:
        encrypted_balance = f.read()
        decrypted_balance = fernet.decrypt(encrypted_balance).decode()
        balance = int(decrypted_balance)



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
    print(f'Number of CPUs: {num_cpus}')
    print(f'The current time is: {time_str}')
    MainMenu = input('''Press 1 to login or 2 to exit Press 3 for balance: ''')

    if MainMenu == '1':
        # Generate and solve the equation as before
        (Answer) = input(f"{Quest1} {Space1} {mid} {Space1} {Quest2}")
        if  int(Answer) == Z:
            global balance 
            balance += 5
            for i in tqdm(range(100)):
                time.sleep(1)
            print("mined a block")
            encrypted_balance = fernet.encrypt(str(balance).encode())
            with open('wallet.bin', 'wb') as f:
                f.write(encrypted_balance)
            print("balance: " + str(balance))
            print("Balance updated to wallet.bin file")
       
    elif MainMenu == '2':
        print("You have " + str(balance) + " coins")
        print("Exiting program. Balance was saved to wallet.bin file")
    
        exit()
while True:
  main()
  
