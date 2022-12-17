import random
import os
import dotenv
from cryptography.fernet import Fernet

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
        balance = (decrypted_balance)

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
    MainMenu = input('Press 1 to login or 2 to exit Press 3 for balance: ')

    if MainMenu == '1':
        # Generate and solve the equation as before
        Answer = input(f"{Quest1} {Space1} {mid} {Space1} {Quest2}")
        # Get user input and convert it to an integer
        # Compare Answer to Z and increment balance if correct
        if Answer == Z:
            print("Mined a block")
            global balance
            balance += 5
            print(f'Your balance is: ${balance}')
        else:
            print("error,block not rewarded")
  
        # Handle ValueError if user input cannot be converted to an integer
        print("Invalid input. Answer must be an integer.")
    elif MainMenu == '2':
        # Save balance to wallet.bin
        encrypted_balance = fernet.encrypt(str(balance).encode())
        with open('wallet.bin', 'wb') as f:
            f.write(encrypted_balance)
        print("Balance saved to wallet")
        return  # Return from the main() function to exit the while loop
    elif MainMenu == '3':
        print("https://github.com/goosecrash/zeuslink2/tree/main/README.md")
        return  # Return from the main() function to exit the while loop
    elif MainMenu == '4':  # new menu option to print balance
        print(f'Your balance is: ${balance:.0f}')
        return  # Return from the main() function to exit the while loop

# Main loop
while True:
    main()
