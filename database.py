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

# Commit the changes to the database
conn.commit()
