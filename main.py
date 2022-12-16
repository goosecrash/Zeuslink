import random
import os
import dotenv

# Declare variables and functions outside of the while loop to avoid
# recreating them every iteration
operations = ['+', '-', '*', '/']  # list of possible operations
numbers1 = [random.randint(1, 100) for _ in range(6)]  # list of 6 random integers from 1 to 1000
numbers2 = [random.randint(1, 100) for _ in range(6)]  # list of 6 random integers from 1 to 1000
balance = 0

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
   
    if MainMenu == '1':
         # Generate and solve the equation as before
        print(f"{Quest1} {Space1} {mid} {Space1} {Quest2}")
        Answer = int(input())  # convert user input to integer
        if Answer == Z:  # compare Answer to Z directly
            print("Mined a block")
            global balance
            balance += 5
            print(f'Your balance is: ${balance:.0f}')
        else:
            print("error,block not rewar")
    elif MainMenu == '2':
        # Save balance to wallet.env file on exit
        with open('wallet.env', 'w') as f:
            f.write(f'BALANCE={balance}')
        print("Balance saved to wallet")
        exit()
    elif MainMenu == '4':
        print("https://github.com/goosecrash/zeuslink2/tree/main/README.md")
    elif MainMenu == '3':  # new menu option to print balance
        print(f'Your balance is: ${balance:.0f}')

# Load .env file with balance if it exists
if os.path.exists('wallet.env'):
    dotenv.load_dotenv('wallet.env')
    balance = int(os.environ.get('BALANCE'))

while True:
  main()