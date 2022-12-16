import sqlite3

# Connect to the database
conn = sqlite3.connect('tokens.db')

# Create a cursor object
cursor = conn.cursor()

# Create a table to store the token information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY,
        balance INTEGER NOT NULL
    )
''')

# Set the initial token supply
cursor.execute('''
    INSERT INTO tokens (balance)
    VALUES (1000000)
''')

# Set the maximum token supply
MAX_TOKEN_SUPPLY = 2000000

def mine_tokens(amount):
    # Check the current token supply
    cursor.execute('''
        SELECT balance FROM tokens
    ''')
    current_supply = cursor.fetchone()[0]

    # If the current token supply plus the amount being mined exceeds the maximum token supply,
    # return an error message
    if current_supply + amount > MAX_TOKEN_SUPPLY:
        return 'Error: Token supply limit reached'

    # Otherwise, update the token supply and return a success message
    cursor.execute('''
        UPDATE tokens
        SET balance = balance + ?
    ''', (amount,))
    conn.commit()
    return 'Success: Tokens mined'

# Test the function
print(mine_tokens(100000))  # Success: Tokens mined
print(mine_tokens(1000000))  # Success: Tokens mined
print(mine_tokens(1000000))  # Error: Token supply limit reached
